from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.authtoken.models import Token

from .serializers import ProfileSerializer
from .models import Profile


class LoginView(APIView):
    def post(self, request):
        user = User.objects.get(
            email=request.data.get("username"), password=request.data.get("password")
        )

        if user is None:
            user = User.objects.get(
                username=request.data.get("username"),
                password=request.data.get("password"),
            )

        if user is not None:
            login(request, user)
            return JsonResponse({"answer": "ok"})
        else:
            return JsonResponse({"answer": "no"})


class RegisterView(APIView):
    def post(self, request):
        try:
            user = User(
                # username=request.data.get(''),
                username="x",
                email=request.data.get("email"),
                password=request.data.get("password"),
            )
            user.save()

            profile = Profile(user=user)
            profile.save()

            is_created = True
        except Exception as ex:
            print(ex)
            is_created = False

        if is_created is True:
            return JsonResponse({"answer": "ok"})
        else:
            return JsonResponse({"answer": "no"})


class ProfileView(APIView):
    def get(self, request):
        profile = Profile.objects.filter(
            user_id=request.user.pk
        )

        serializer = ProfileSerializer(
            profile,
            many=True
        )

        return JsonResponse(
            serializer.data,
            safe=False
        )

    def post(self, request, format=None):
        user = request.user

        if not user.is_authenticated:
            return JsonResponse({})

        profile = Profile.objects.get(
            user_id=request.user.pk
        )

        user.first_name = request.data.get('first_name')
        user.last_name = request.data.get('last_name')
        user.email = request.data.get('email')
        profile.country = request.data.get('country')
        profile.region = request.data.get('region')
        profile.city = request.data.get('city')
        profile.post_code = request.data.get('post_code')
        profile.address_line_1 = request.data.get('address_line_1')
        profile.address_line_2 = request.data.get('address_line_2')
        profile.phone_number = request.data.get('phone_number')

        user.save()
        profile.save()
        return JsonResponse({"answer": "ok"})


class IsAuthenticatedView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return JsonResponse({"answer": "authenticated"})
        else:
            return JsonResponse({"answer": "not authenticated"})


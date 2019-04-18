from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.authtoken.models import Token

from .serializers import ProfileSerializer
from .models import Profile

class LoginView(APIView):
    def post(self, request):
        user = User.objects.get(
            email=request.data.get('username'),
            password=request.data.get('password')
        )

        if user is None:
            user = User.objects.get(
                username=request.data.get('username'),
                password=request.data.get('password')
            )

        if user is not None:
            login(request, user)
            return JsonResponse({
                'answer': 'ok'
            })
        else:
            return JsonResponse({
                'answer': 'no'
            })


class RegisterView(APIView):
    def post(self, request):
        try:
            user = User(
                # username=request.data.get(''),
                username='x',
                email=request.data.get('email'),
                password=request.data.get('password')
            )
            user.save()

            profile = Profile(
                user=user
            )
            profile.save()

            is_created = True
        except Exception as ex:
            print(ex)
            is_created = False

        if is_created is True:
            return JsonResponse({
                'answer': 'ok'
            })
        else:
            return JsonResponse({
                'answer': 'no'
            })

class ProfileView(APIView):
    def get(self, request):
        profile = Profile.objects.filter(
            user=request.user
        )
        serializer = ProfileSerializer(
            profile,
            many=True
        )

        return JsonResponse(
            serializer.data,
            safe=False
        )

class IsAuthenticatedView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return JsonResponse({
                'answer': 'authenticated'
            })
        else:
            return JsonResponse({
                'answer': 'not authenticated'
            })
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.views import APIView
# from rest_framework.generics import CreateAPIView

class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )

        if user is not None:
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
            user = User.objects.create_user(
                username=request.data.get('email'),
                email=request.data.get('email'),
                password=request.data.get('password')
            )
            user.save()

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

from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.views import APIView

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

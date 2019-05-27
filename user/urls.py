from django.urls import path

from .views import LoginView,  \
    RegisterView,   \
    IsAuthenticatedView,    \
    ProfileView
    # IsEmailAvailable

urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('authenticate', IsAuthenticatedView.as_view()),
    path('profile', ProfileView.as_view()),
    # path('isEmailAvailable/<str:email>', IsEmailAvailable.as_view())
]

from django.urls import path
from .views import RegisterAPIView, LoginAPIView

app_name = 'authentication'

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
]

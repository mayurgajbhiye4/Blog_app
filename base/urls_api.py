from django.urls import path 
from .views_api import *


urlpatterns = [
    path('login/', LoginView.as_view(), name='loginview'),
    path('register/', RegisterView.as_view(), name='registerView')
]       
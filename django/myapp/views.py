from django.shortcuts import render
from .serializers import BotUserSerializer
from .models import *
from rest_framework.generics import ListCreateAPIView

class BotUsersApiView(ListCreateAPIView):
    queryset = Bot_User.objects.all()
    serializer_class = BotUserSerializer

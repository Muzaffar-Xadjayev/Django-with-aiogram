from django.urls import path
from .views import *

urlpatterns = [
    path('users',BotUsersApiView.as_view(),name="user_page")
]
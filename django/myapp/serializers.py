from .models import *
from rest_framework.serializers import ModelSerializer

class BotUserSerializer(ModelSerializer):
    class Meta:
        model=Bot_User
        fields=("user_id","name","username","created_at")

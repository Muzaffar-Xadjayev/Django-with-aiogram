from django.db import models

# Create your models here.
class Bot_User(models.Model):
    user_id=models.CharField(max_length=100, unique=True)
    name=models.CharField(max_length=500)
    username=models.CharField(max_length=150, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="User"


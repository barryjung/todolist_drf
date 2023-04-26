from django.db import models
from user.models import UserModel


class Todo(models.Model):
    title = models.CharField(max_length=256)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

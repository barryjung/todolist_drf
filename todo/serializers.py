from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title"]


class TodoEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "is_complete"]

    def update(self, instance, validated_data):
        todo = super().update(instance, validated_data)
        if todo.is_complete:
            todo.completion_at = todo.updated_at
        else:
            todo.completion_at = None
        todo.save()
        return todo

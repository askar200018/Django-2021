from rest_framework import serializers
from main.models import Todo, Task


class TodoSerializer(serializers.ModelSerializer):
    todos = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = '__all__'


class TodoDetailSerializer(serializers.ModelSerializer):
    todos = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = ('name', 'tasks', )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task', 'mark', 'lists_id')


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

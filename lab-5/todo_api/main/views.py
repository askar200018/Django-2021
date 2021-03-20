from django.shortcuts import render
from rest_framework import viewsets, renderers, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .serializers import TodoSerializer, TodoDetailSerializer, TaskSerializer, TaskDetailSerializer
from main.models import Todo, Task


class ListViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'create':
            return TodoSerializer
        else:
            return TodoDetailSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def tasks_by_list(self, request, pk):
        queryset = Todo.objects.filter(lists_id=pk)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'create':
            return TaskSerializer
        else:
            return TaskDetailSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny, ))
    def completed(self, request, pk):
        queryset = Task.objects.filter(mark=False)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)



from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.todos, name='todos'),
    path('todos/<int:todo_id>/completed/', views.completed_todos, name='completed_todos')
]
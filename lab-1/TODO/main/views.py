from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

class Todo:
    def __init__(self, name, created_date, expire_date, owner):
        self.name = name
        self.created_date = created_date
        self.expire_date = expire_date
        self.owner = owner


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def todos(request):
    res_todos = [Todo('Task 1', '10/09/2018', '12/09/2018', 'admin'),
                Todo('Task 2', '10/09/2018', '12/09/2018', 'admin'),
                Todo('Task 3', '10/09/2018', '12/09/2018', 'admin'),
                Todo('Task 4', '10/09/2018', '12/09/2018', 'admin'),
                Todo('Task 5', '10/09/2018', '12/09/2018', 'admin')]
    return render(request, 'main/todo_list.html', {'todos': res_todos})


def completed_todos(request, todo_id):
    res_todos = [Todo('Task 1', '10/09/2018', '12/09/2018', 'admin')]
    return render(request, 'main/completed_todo_list.html', {'todos': res_todos})



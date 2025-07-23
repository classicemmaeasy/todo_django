from django.shortcuts import redirect, render
from . models import Task
from django.http import HttpResponse
from .models import Task
# Create your views here.


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    print(tasks)

    # context = {
    #     'my_task': tasks
    # } 
    return render(request, 'home.html', {'all_task': tasks})


def add(request):
    task = request.POST['task']
    Task.objects.create(task=task, is_completed=False)
    return redirect('/')
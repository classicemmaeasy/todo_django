from django.shortcuts import get_object_or_404, redirect, render
from . models import Task
from django.http import HttpResponse
from .models import Task
# Create your views here.


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    print(tasks)

    completed_tasks = Task.objects.filter(is_completed=True)
    print(completed_tasks)

    context = {
        'all_task': tasks,
        'completed_tasks': completed_tasks
    } 
    return render(request, 'home.html', context)


def add(request):
    task = request.POST['task']
    Task.objects.create(task=task, is_completed=False)
    return redirect('/')


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('/')



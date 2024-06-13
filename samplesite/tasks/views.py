from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def task_list_and_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, 'task_list_and_create.html', {'tasks': tasks, 'form': form})




from django.shortcuts import render, redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'CRM_app/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        task = Task()
        task.category = request.POST.get('category')
        task.task_description = request.POST.get('task_description')
        task.start_date = request.POST.get('start_date')
        task.deadline = request.POST.get('deadline')
        task.executor_name = request.POST.get('executor_name')
        task.save()
        return redirect('task_list')
    return render(request, 'CRM_app/add_task.html')


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.category = request.POST.get('category')
        task.task_description = request.POST.get('task_description')
        task.start_date = request.POST.get('start_date')
        task.deadline = request.POST.get('deadline')
        task.executor_name = request.POST.get('executor_name')
        task.save()
        return redirect('task_list')
    return render(request, 'CRM_app/update_task.html', {'task': task})


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')

from django.shortcuts import render, redirect

from .models import ListOfTasks, Task

# Create your views here.

def list(request):
    allLists = ListOfTasks.objects.order_by('-createAt')
    context = {
        'allLists': allLists,
    }
    return render(request,'todozim/list.html',context)

def createList(request):
    inputTitle = request.POST.get('titleList')
    newlist = ListOfTasks.objects.create(title=inputTitle)
    newlist.save()
    return render(request,'todozim/list.html')

def detail(request, id_list):
    exist_list = ListOfTasks.objects.get(pk=id_list)
    all_tasks = Task.objects.filter(listTasks=id_list)
    context = {
        'exist_list': exist_list,
        'all_tasks': all_tasks,
    }
    return render(request,'todozim/details.html', context)

def add_task(request, id_list):
    exist_list = ListOfTasks.objects.get(pk=id_list)
    input_task = request.POST['add_task']
    new_task = Task.objects.create(description=input_task, listTasks=exist_list)
    new_task.save()
    return redirect('detail', exist_list.id)

def update_done_task(request, id_task, status_task):
    exist_task = Task.objects.get(pk=id_task)
    status = bool(status_task)
    exist_task.done = status
    exist_task.save()
    return redirect('detail', exist_task=exist_task.id)


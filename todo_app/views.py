from django.shortcuts import redirect, render
from todo_app.forms import TodoForm

from todo_app.models import Task

# Create your views here.
def index(req):
    task1 = Task.objects.all()
    if req.method == 'POST':
        name = req.POST.get('task','')
        priority = req.POST.get('priority','')
        date = req.POST.get('date','')
        task = Task(name=name,priority=priority,date=date)
        task.save()

    return render(req,'index.html',{'task1':task1})
def update(req,id):
    task = Task.objects.get(id = id)
    f = TodoForm(req.POST or None,instance = task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(req,'edit.html',{'f':f,'task':task})
    
# def details(req):
#     task = Task.objects.all()
#     return render(req,'details.html',{'task': task})

def delete(req,task_id):
    task = Task.objects.get(id = task_id)
    if req.method == 'POST':
        task.delete()
        return redirect('/')
    return render(req,'delete.html')
from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Task
from .forms import TaskForm,CompleteTaskForm,ScrapbookDateForm


# helper utils
class Developer():
    def __init__(self,name,pos,pic,gitlink) -> None:
        self.name = name 
        self.position = pos
        self.picture = pic
        self.gitlink = gitlink





# Create your views here.
def homeView(request):
    context = {}
    return render(request,"home.html",context)


def aboutView(request):
    prasanna = Developer('R Prasannavenkatesh','Backend Dev','https://avatars0.githubusercontent.com/u/54119123?s=400&u=f08e1a3b2cb36bd9ebda9dd40f1c6c97f7ed3fa2&v=4','https://github.com/hanzohasashi33')
    vijay = Developer('Vijay Jaisankar','Frontend Dev','https://avatars3.githubusercontent.com/u/56185979?s=400&u=65beb118f34e21c0acb0d56ed98f75b11e1647bc&v=4','https://github.com/vijay-jaisankar')
    shrey = Developer('Shrey Tripathi','Full Stack Dev','https://avatars.githubusercontent.com/u/52366674?s=460&u=fa0b3dc026bd6167e892fffc7588455ff68ef972&v=4','https://github.com/shrey27tri01')
    context = {"prasanna":prasanna,"vijay":vijay,"shrey":shrey}
    return render(request,"about.html",context)


@login_required
def taskListView(request):
    tasks = Task.objects.all().filter(author=request.user,complete=False)
    context = {"tasks":tasks}
    return render(request,"tasks/list.html",context)


@login_required
def createNewTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.author = request.user
            new_task.save()
        return redirect('/list/')
    context = {"form":form}
    return render(request,"tasks/new.html",context)


@login_required
def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/list/')
    context = {"task":task,"form":form}
    return render(request,"tasks/update.html",context)


@login_required
def deleteTask(request,pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/list/')
    context = {"task":task}
    return render(request,"tasks/delete.html",context)

@login_required
def completeTask(request,pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = CompleteTaskForm(request.POST,request.FILES)
        # print("post form")
        if form.is_valid():
            # form.save()
            # print("cleaned data")
            cd = form.cleaned_data
            # print(cd)
            task.completed_picture = cd['completed_picture']
            task.complete = True
            task.save()
            return redirect('/list/')
    else:
        form = CompleteTaskForm()
        # print("get form")
    context = {"task":task,"form":form}
    return render(request,"tasks/complete.html",context)


@login_required
def scrapbookFormView(request):
    form = ScrapbookDateForm()
    if request.method == 'POST':
        form = ScrapbookDateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # print(cd)
            print(cd['scrapBook_date'].year,cd['scrapBook_date'].month,cd['scrapBook_date'].day)
            return redirect(reverse('scrapbook',kwargs={'year':cd['scrapBook_date'].year,'month':cd['scrapBook_date'].month,'day':cd['scrapBook_date'].day}))
            # print(requrl)
    else:
        form = ScrapbookDateForm()
    context = {"form":form}
    return render(request,"tasks/scrapbookForm.html",context)


@login_required
def scrapbookView(request,year,month,day):
    tasks = Task.objects.all().filter(created__year=year,created__month=month,created__day=day,complete=True,author=request.user)
    print(tasks)
    context = {"tasks":tasks,"day":day,"month":month,"year":year}
    return render(request,"scrapbook/scrapbook.html",context)
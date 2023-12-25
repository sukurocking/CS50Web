from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

task_list = ["bring grocery", "bring some eggs"]



class TaskForm(forms.Form):
    task = forms.CharField(max_length=255)

# Create your views here.
def index(request):
    return render(request,template_name="tasks/index.html", context={"tasks_list": task_list})

def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.cleaned_data['task']
            task_list.append(new_task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            form = TaskForm()
    return render(request, template_name="tasks/add.html", context={"form": form})
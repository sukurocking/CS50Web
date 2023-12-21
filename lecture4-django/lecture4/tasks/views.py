from django.shortcuts import render
# from django.http import HttpResponse
from django import forms

task_list = ["bring grocery", "bring some eggs"]

class TaskForm(forms.Form):
    task = forms.CharField(max_length=255)

# Create your views here.
def index(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.cleaned_data['task']
            task_list.append(new_task)
        else:
            form = TaskForm()
    return render(request,template_name="tasks/index.html", context={"tasks_list": task_list, "form": form})

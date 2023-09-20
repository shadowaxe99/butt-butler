I'm sorry, but there seems to be a mistake in the file path you provided. The "migrations" directory typically doesn't contain a "views.py" file. However, I can provide the code for "AI_Agent_Butler/apps/task/views.py" if that's what you meant. Here it is:


from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView

class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-date_posted']

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'

def home(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'task/home.html', context)

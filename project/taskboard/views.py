from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from funfactory.urlresolvers import reverse
from project.taskboard.forms import TaskForm
from project.taskboard.models import Task


class CreateTask(CreateView):
    form_class = TaskForm
    template_name = 'taskboard/edit_task.html'
    model = Task

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user.get_profile()
        return super(CreateTask, self).form_valid(form)

    def get_success_url(self):
        return reverse('list_tasks')


class EditTask(UpdateView):
    form_class = TaskForm
    template_name = 'taskboard/edit_task.html'
    model = Task
    context_object_name = 'task'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        self.kwargs = kwargs
        task = self.get_object()
        if task.user_can_edit(user):
            return super(EditTask, self).dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()

    def get_context_data(self, **kwargs):
        context = super(EditTask, self).get_context_data(**kwargs)
        context['cancel_url'] = reverse('view_task',
                                        kwargs={'slug': self.object.slug})
        return context

    def get_success_url(self):
        return reverse('view_task', kwargs={'slug': self.object.slug})


class ViewTask(DetailView):
    model = Task
    template_name = 'taskboard/view_task.html'


class ListTasks(ListView):
    queryset = Task.objects.filter(disabled=False)
    template_name = 'taskboard/list_tasks.html'


class UserTasks(ListView):
    template_name = 'taskboard/list_tasks.html'

    def get_queryset(self):
        username = self.kwargs.get('username', None)
        user = get_object_or_404(UserProfile, user__username=username)
        queryset = Task.objects.filter(user=user)
        return queryset

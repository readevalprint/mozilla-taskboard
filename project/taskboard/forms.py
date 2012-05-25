from django import forms
from project.taskboard.models import Task
from tower import ugettext_lazy as _lazy
from ajax_select.fields import AutoCompleteSelectField


class TaskForm(forms.ModelForm):
    # TODO - Make contacts (users) autocomplete
    instructions = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _lazy('Tell us all about it...')}))

    contact = AutoCompleteSelectField('userprofile',
                                      required=True, help_text=None)

    class Meta:
        model = Task
        exclude = ['assigned_to', 'assigned', 'created_by', 'slug']


class TakeTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['assigned_to']

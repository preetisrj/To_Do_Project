from django import forms
from django.forms import ModelForm

from .models import *


class ToDoForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task title...'}))
	task_detail = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task details...'}))
	

	class Meta:
		model = ToDo
		fields = ('title', 'task_detail', 'complete')

from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.urls import reverse

# Create your views here.
def index(request):

	tasks = ToDo.objects.all()

	form = ToDoForm()

	if request.method == 'POST':
		form = ToDoForm(request.POST)
		if form.is_valid():
			form.save()
	context = {'tasks': tasks, 'form': form}
	return render(request, 'To_Do/index.html', context)


def update_To_Do(request, pk):
	task = ToDo.objects.get(id=pk)

	form = ToDoForm(instance=task)

	if request.method == 'POST':
		form = ToDoForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('To_Do:index'))

	context = {'form': form}
	return render(request, 'To_Do/update_To_Do.html', context)
	

def delete_To_Do(request, pk):
	item = ToDo.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return HttpResponseRedirect(reverse('To_Do:index'))

	context = {'item': item}
	return render(request, 'To_Do/delete_To_Do.html', context)

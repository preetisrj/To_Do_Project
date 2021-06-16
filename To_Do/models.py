from django.db import models


# Create your models here.


class ToDo(models.Model): 
	title = models.CharField(max_length=200)
	task_detail = models.TextField(max_length=500, default=False)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title


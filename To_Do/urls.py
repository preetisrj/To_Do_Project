from django.conf.urls import url
from django.urls import path
from To_Do import views

app_name = "To_Do"

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<str:pk>/', views.update_To_Do, name="update_task"),
   	path('delete/<str:pk>/', views.delete_To_Do, name="delete"),
]


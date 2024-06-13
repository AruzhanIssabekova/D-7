from django.urls import path
from . import views
from .views import task_list_and_create
urlpatterns = [
    path('', task_list_and_create, name='task_list'),
]

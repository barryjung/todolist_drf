from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoView.as_view(), name='todo_view'),
    path('<int:todo_id>', views.TodoView.as_view(), name='todo_id_view'),
]

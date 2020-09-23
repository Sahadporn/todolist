from django.urls import path
from . import views

app_name = 'todoList'
urlpatterns = [
    path('', views.todoView, name='index'),
    path('addTodo/', views.addTodo),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo)
]

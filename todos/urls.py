from django.urls import path

from . import views

urlpatterns = [
    path('', views.todos_list_view, name='todos_list'),
    path('<int:pk>/', views.todo_detail_view, name='todo_detail'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.todos_list_view, name='todos_list'),
    path('<int:pk>/', views.todo_detail_view, name='todo_detail'),
    path('create/', views.todo_add_view, name='todo_create'),
    path('<int:pk>/update/', views.todo_update_view, name='todo_update'),
    path('<int:pk>/checkbox/', views.todo_update_checkbox, name='todo_update_ckeckbox'),
    path('<int:pk>/delete/', views.todo_delete_view, name='todo_delete'),
]

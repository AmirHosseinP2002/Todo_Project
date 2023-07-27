from django.urls import path

from . import views

urlpatterns = [
    path('', views.todos_list_view, name='todos_list'),
]

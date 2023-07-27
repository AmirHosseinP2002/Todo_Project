from django.shortcuts import render
from django.http import HttpResponse


def todos_list_view(request):
    return HttpResponse('Hello')

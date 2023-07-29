from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Todo
from .forms import TodoForm


@login_required
def todos_list_view(request):
    todos = Todo.objects.filter(author=request.user).order_by('-datetime_created')
    return render(request, 'todos/todos_list.html', {
        'todos': todos
    })


@login_required
def todo_detail_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todos/todo_detail.html', {
        'todo': todo,
    })


@login_required
def todo_add_view(request):
    if request.method == 'POST':
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            obj = todo_form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('todos_list')
    else:
        todo_form = TodoForm()
    return render(request, 'todos/todo_create.html', {
        'todo_form': todo_form,
    })


@login_required
def todo_update_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo_form = TodoForm(instance=todo)
    if request.method == 'POST':
        todo_form = TodoForm(request.POST or None, instance=todo)
        if todo_form.is_valid():
            todo_form.save()
            return redirect(reverse('todo_detail', args=[todo.id]))

    return render(request, 'todos/todo_update.html', {
        'todo_form': todo_form,
        'todo': todo
    })


@login_required
def todo_delete_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect(reverse('todos_list'))

    return render(request, 'todos/todo_delete.html', {
        'todo': todo,
    })


@login_required
def todo_update_checkbox(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    is_completed = request.POST.get('is_completed', False)
    print(is_completed)
    if is_completed == 'on':
        is_completed = True

    todo.is_completed = is_completed
    todo.save()
    return redirect('todos_list')


@login_required
def todo_delete_icon(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todos_list')

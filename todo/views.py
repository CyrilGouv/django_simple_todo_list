from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

def todo_list(request) :
    todos = Todo.objects.all()
    
    context = {
        'todo_list': todos
    }

    return render(request, 'todo_list.html', context)


### CRUD

# Retrieve
def todo_detail(request, id) :
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }

    return render(request, 'todo_detail.html', context)


# Create
def todo_create(request) :
    form = TodoForm(request.POST or None)

    if form.is_valid() :
        # Create a todo object
        form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'todo_create.html', context)



# Update
def todo_update(request, id) :
    todo = Todo.objects.get(id=id)

    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid() :
        # Create a todo object
        form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'todo_update.html', context)




# Delete
def todo_delete(request, id) :
    todo = Todo.objects.get(id=id)
    todo.delete()

    return redirect('/')
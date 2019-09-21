from cgitb import text

from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import BookForm
from webapp.models import Book, STATUS

def index_view(request, *args, **kwargs):
    appends = Book.objects.all()
    return render(request, 'index.html', context={
        'appends': appends
    })


def form_storage_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'form.html', context={
            'form': form,
            'status': STATUS
        })
    elif request.method == 'POST':
        form = BookForm(data=request.POST)

        if not form.is_valid():
            return render(request, 'form.html', context={'form': form, 'status': STATUS})

        Book.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            text=form.cleaned_data['text'],

        )
        return redirect('index')

def detailed_update_view(request, pk):
    task = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(data={
            'name': task.name,
            'email': task.email,
            'text': text,
        })
        return render(request, 'update.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            task.name = form.cleaned_data['name']
            task.email = form.cleaned_data['email']
            task.text = form.cleaned_data['text']
            task.save()
            return redirect('index')

        return render(request, 'update.html', context={'form': form, 'task': task})



def detailed_delete_view(request, pk):
    task = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
       return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TodoForm, UserRegForm
from .models import Todo

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = UserRegForm()
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)

@login_required
def home(request):
    item_list = Todo.objects.filter(name=request.user.username).order_by("-date")
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid() and form['name'].value() == request.user.username:
            form.save()
        return redirect('home')

    form = TodoForm(initial={'name': request.user.username})
    context = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'index.html', context)

@login_required
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed")
    return redirect('home')
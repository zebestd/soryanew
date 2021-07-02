from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required



from django.contrib.auth.models import User

# Create your views here.
def soryalist(request):
    soru = Soru.objects.all()
    
    return render(request, 'home.html', {'soru': soru})


def createSoru(request):
    form = SoruForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = SoruForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'form.html', context)

def sorular(request, pk_test):
    sorus = Soru.objects.get(id=pk_test)
    try:
        yanits = Yanit.objects.get(id=pk_test)
    except Yanit.DoesNotExist:
        yanits = None

    form = YanitForm(request.POST)
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = YanitForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save()
            return redirect('/')
    context = {'sorus':sorus, 'yanits':yanits, 'form':form}
    return render(request, 'sorular.html',context)  
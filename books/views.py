from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def home(request):
    books = Book.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        books = Book.objects.filter(title__icontains=search)
        
        results = Book.objects.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )
        
        context = {
            'books': books,
            'results': results,
        }
        return render(request, 'home.html', context)
    
    context = {
        'books': books,
    }
    
    return render(request, 'home.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
       if request.POST['password1'] == request.POST['password2']:
            try:
               user = User.objects.get(username=request.POST['username'])
               return render(request, 'signup.html', {'error': 'Username already exists'})
            except User.DoesNotExist:
               user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
               auth.login(request, user)
               return redirect('home')
    else:
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    else:
        return render(request, 'home.html')
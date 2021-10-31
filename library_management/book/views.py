from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Books
from .forms import Signupform,Loginform,Bookform

# Create your views here.

def home(request):
    book = Books.objects.all()
    return render(request,'home.html',{'books':book})

def dashboard(request):
    if request.user.is_authenticated:
        book = Books.objects.all()
        return render(request, 'dashboard.html', {'books': book})
    else:
        return HttpResponseRedirect('/login')

def admin_signup(request):
    if request.method == 'POST':
        check1 = False
        check2 = False
        check3 = False
        form = Signupform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            if password1 != password2:
                check1 = True
                messages.error(request, 'Password doesn\'t matched')
            if User.objects.filter(username=username).first():
                check2 = True
                messages.error(request, 'Username already exists')
            if User.objects.filter(email=email).exists():
                check3 = True
                messages.error(request, 'Email already registered')
            if check1 or check2 or check3:
                return redirect('/signup')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                messages.success(
                    request, f'Thanks for registering {user.username}!')
                return redirect('/login')


    else:
        form = Signupform()
    return render(request, 'signup.html', {'form': form})


def admin_login(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            form = Loginform(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in successfully')
                    return HttpResponseRedirect('/dashboard')
            else:
                messages.error(request, 'Invalid username and password!!')
        else:

            form = Loginform()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard')


def admin_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def add_book(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            post=Bookform(request.POST)
            if post.is_valid():
                title=post.cleaned_data['title']
                check_book = Books.objects.filter(title=title).first()
                if check_book:
                    messages.success(request, ' Book is already exits!!')
                    return render(request, 'addpost.html')
            messages.success(request,'Your Book is Added! Please Go To The Dashboard')
            post.save()
        else:
            post=Bookform()
        return render(request, 'addpost.html',{'add':post})
    else:
        return HttpResponseRedirect('/login')

def update_book(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            ip=Books.objects.get(pk=id)
            update=Bookform(request.POST,instance=ip)
            if update.is_valid():
                messages.info(request,'Book is updated.....!!!')
                update.save()
        else:
            ip=Books.objects.get(pk=id)
            update=Bookform(instance=ip)
        return render(request, 'updatepost.html',{'update':update})
    else:
        return HttpResponseRedirect('/login')



def delete_book(request, id):
    if request.user.is_authenticated:
        if request.method=='POST':
            ip=Books.objects.get(pk=id)
            ip.delete()
            return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')






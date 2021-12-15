from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash,authenticate,login,logout
from .models import Blog
from django.contrib import messages
from django.core.mail import send_mail
from . forms import BlogForm
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def home(request):
    blog = Blog.objects.all()
    return render(request, 'home.html', {'blog':blog})

def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email Already Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.warning(request, 'Username Already Taken')
                return render('register')
            
            else:
                user =  User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username)
                user.save()
                messages.success(request, 'User has been registered')
                return redirect('login')
        else:
            messages.warning(request, 'Password did not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:   
            login(request, user)
            return redirect('/')
            
        else:
            messages.warning(request,'Invalid credentials')
            return redirect('login')    
    return render(request,'login.html') 


def user_logout(request):
    logout(request)
    return redirect('home')


def details(request,id):
    blog = Blog.objects.get(id=id)
    return render(request, 'pagedetails.html', {'blog':blog})

def user_post(request):
    if request.method=='POST':
        tittle = request.POST.get('tittle')
        dsc = request.POST.get('dsc')
        img = request.FILES['img']
        post = Blog(tittle=tittle, dsc=dsc, user_id=request.user, Img=img)
        post.save()
        messages.success(request,'Posted')
        return redirect('home')
    return render(request, 'post.html')

def delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request, 'Post has been deleted successfuly')
    return redirect('home')

def edit(request,id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(instance=blog)
    if request.method=='POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Edited successfully')
            return render('home')
    return render(request, 'edit.html', {'form':form})
    
def search(request):
    sname = request.POST['sname']
    form = Blog.objects.filter(tittle__icontains=sname)
    return render(request, 'home.html',{'form':form})
    


def changepassword(request):
    if request.method=='POST':
        cform = PasswordChangeForm(request.user, request.POST)
        if cform.is_valid():
            user = cform.save()
            update_session_auth_hash(request, user)
            messages.success(request, ' password has been changed successfully')
            return redirect('home')
        else:
            messages.warning(request, 'error')
            return redirect('changepassword.html')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'changepassword.html', {'form':form})
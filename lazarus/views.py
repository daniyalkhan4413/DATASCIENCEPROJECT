from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JobPosting, User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def Homeview(request):
    jobs = JobPosting.objects.all()

    return render(request, template_name='lazarus/home.html', context={'jobs': jobs})


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('homeview')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:

            user = User.objects.get(username=username)

        except:
            messages.error(request, "User Does not exist Please check again ")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homeview')
        else:
            messages.error(request, "Username or Password is Not right")

    return render(request, template_name='lazarus/login.html')


def registration(request):
    return render(request, template_name='lazarus/Registration.html')


def JobView(request, pk):
    ViewedJob = JobPosting.objects.get(id=pk)

    return render(request, template_name='lazarus/Jobview.html', context={'ViewedJob': ViewedJob})

@login_required(login_url='login')
def logoutfunction(request):

    logout(request)
    return redirect('login')
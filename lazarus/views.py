from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JobPosting, User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .form import myusercreationform, Userform


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



    if request.method == "POST":

        form = myusercreationform(request.POST)
        email = request.POST.get('email')

        username = request.POST.get('username')

        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if password1 != password2:
            messages.error(request,'Password Did Not Match')
            return render(request, 'lazarus/Registration.html', {'form': form})


        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Address Already Exist')

            return render(request, 'lazarus/Registration.html', {'form': form})

        if User.objects.filter(username=username).exists():
            messages.error(request,'Username Already Exist')
            return render(request, 'lazarus/Registration.html', {'form': form})

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')  # Or any page you want to redirect to



    else:
        form = myusercreationform()

    print('failed1')

    return render(request, template_name='lazarus/Registration.html',context={'form':form})

@login_required(login_url='login')
def JobView(request, pk):
    ViewedJob = JobPosting.objects.get(id=pk)

    return render(request, template_name='lazarus/Jobview.html', context={'ViewedJob': ViewedJob})

@login_required(login_url='login')
def logoutfunction(request):

    logout(request)
    return redirect('login')

@login_required(login_url='login')
def UpdateUser(request):

    user = request.user
    form = Userform(instance=user)

    UserInstance = User.objects.get(id=request.user.id)




    if request.method=="POST":
        form = Userform(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('homeview')

    ctx = {'form':form,'userinstance':UserInstance}
    return render(request,'lazarus/UpdateUser.html',ctx)
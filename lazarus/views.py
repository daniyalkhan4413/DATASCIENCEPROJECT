from django.shortcuts import render,redirect
# Create your views here.
def Homeview(request):

    return render(request,template_name='lazarus/home.html')



def login(request):


    if request.method == 'POST':

        return redirect('homeview')



    return render(request,template_name='lazarus/login.html')



def registration(request):

    return render(request,template_name='lazarus/Registration.html')



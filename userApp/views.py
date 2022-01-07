from django.http import HttpResponse

from .forms import Userauth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as loginauth, logout as logoutsite,authenticate
from django.shortcuts import render, redirect
from .forms  import SignUpForm,User, userProfileForm
from .models import Profile

# Create your views here.

def baseView(request):
        return render(request,'base.html')

def home(request):

    return render(request,'project/home.html')

def logOut(request):
    logoutsite(request)

    # return render(request,'demo/login.html')
    return redirect('base')




# def viewuser(request):

#     return render(request, 'demo/viewuser.html')

def viewuser(request):
    # profile = Profile.objects.all()
    profile = Profile.objects.get(user=request.user)
    # print(profile)
    
    return render(request, 'demo/viewuser.html', {'profile':profile})

def userProfileView(request):
    form = userProfileForm()
    if request.method == "POST":
        form = userProfileForm(request.POST)
        if form.is_valid():
            myform = form.save()
            myform.user = request.user
            myform.save()
            return redirect('viewUser')
    return render(request, 'demo/userProfile.html', {'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            loginauth(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'demo/signup.html', {'form': form})


def loginbase(request):
    form = Userauth
    if (request.method == 'GET'):
        return render(request, 'demo/login.html', {'form': form})
    else:
       user = authenticate(username=request.POST['username'],password=request.POST['password'])
       print(user)
       if (user):
           loginauth(request,user)
           return render(request, 'project/home.html')

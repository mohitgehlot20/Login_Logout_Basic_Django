from django.contrib.auth import authenticate,logout,login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
# harry ,harry$$**00
def index(request):
    # return("Index hu bhai")
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, "index.html")

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'login.html')
    return render(request, 'login.html')






def logoutUser(request):
    logout(request)
    # return render (request,'index.html')
    return redirect('/login')
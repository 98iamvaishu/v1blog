from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User


# Create your views here.
def signin(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("succes")
    return render(request,"login.html")

def logout1(request):
    logout(request)

   
def signup(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['pass']
        email = request.POST['email']
        user = User.objects.create_user(username, password, email)
        return HttpResponse("succes")   
    return render(request,"signup.html")        
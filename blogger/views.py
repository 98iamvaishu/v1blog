from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from blogger.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime


# Create your views here.

flag=True
def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email,
                            email=email, password=password)
        if user is not None:
            login(request, user)
            fname = request.user.first_name
            return redirect("/home/", {"user": user})
        else:
            return redirect("/signin1/",)
    return render(request, "login.html")


def logout1(request):
    logout(request)
    return redirect("/home/")


def signup(request):
    if request.method == "POST":
        # username = request.POST.get['name']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['pass']
        email = request.POST['email']
        user = authenticate(request, username=email, email=email,
                            password=password, firstname=fname, lastname=lname)
        if user is None:
            user = User.objects.create_user(username=email, email=email,
                                          password=password, first_name=fname, last_name=lname)
            p = Profile.objects.create(user=user)
            login(request, user)
            return redirect("/home/", {"fname": fname})
            print(name)
        else:
            return HttpResponse("Already exists")
    return render(request, "signup.html")


def main(request):
    posts = Blogsite.objects.all()
    return render(request, "index.html", {"posts": posts})


def home(request):
    posts = reversed(Blogsite.objects.all())
    print(posts)
    user = request.user
    return render(request, "home.html", {"posts": posts,"user":user})


def post_page(request, post_id): 
    user = request.user
    prof  = Profile.objects.get(user=request.user)
    mypost = Blogsite.objects.get(pk=post_id)
    if 'com' in request.POST:
        text = request.POST['comment']
        Comment.objects.create(text =text,post=mypost,profile=prof)
    if 'like' in request.POST:
        mypost.likes = mypost.likes+1
        mypost.save()
    mypost = Blogsite.objects.get(pk=post_id)
    print(mypost.likes)
    comment = reversed(Comment.objects.filter(post=mypost))
    return render(request, "post.html", {"post": mypost, "comment": comment})


def list_post(request):
    posts = Vpost.objects.all()
    return render(request, "list.html")

def profile(request):
    user  = request.user
    prof = Profile.objects.get(user=request.user)
    posts = reversed(Blogsite.objects.filter(author=prof))
    return render(request, "profile.html",{"posts": posts,"user":user,"p" :prof,flag:"flag"})

def profile1(request):
    user = request.user
    posts = reversed(Blogsite.objects.filter(author=user))
    prof = Profile.objects.get(user=user)
    return render(request, "profile.html",{"posts": posts,"user":user,"p" :prof,flag:"flag"})

def view_profile(request):
    user = request.user
    prof = Profile.objects.get(user=user)
    if request.method == 'POST':
        filepath = request.FILES.get('filepath', False)
        status = request.POST['status']
        d = request.POST['desig']
        p1 = Profile.objects.get(user=user)
        p1.pic = filepath
        p1.status = status
        p1.desig = d
        p1.save()
        flag=False
        return redirect("/profile/")
    return render(request, "view_profile.html",{"p":prof})



def new_post(request):
    if request.method == 'POST':
        user = Profile.objects.get(user = request.user)
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        post = request.POST['content']
        duration = request.POST['duration']
        date = datetime.datetime.now()
        bor = Blogsite.objects.create(title=title,likes = 0,subtitle = subtitle,duration=duration, content=post,author = user,date = date)
        return redirect("/home/")
    return render(request, "new_post.html")

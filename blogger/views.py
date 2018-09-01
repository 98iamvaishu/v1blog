from django.shortcuts import render,HttpResponse
from blogger.models import Blogsite,Comment

# Create your views here.
def home(request):
	posts = Blogsite.objects.all()
	print(posts)
	return  render(request,"index.html",{"posts":posts})
def post_page(request,post_id):
	mypost = Blogsite.objects.get(pk = post_id)
	comment =Comment.objects.filter(post =mypost)	
	return render(request,"post.html",{"post":mypost, "comment":comment})
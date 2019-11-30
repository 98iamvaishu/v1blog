from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    pic = models.ImageField(upload_to = 'images', null = True,default='blogger/images/default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length =200)
    desig   = models.CharField(max_length =200,null=True)
class Blogsite(models.Model):
    title = models.CharField(max_length =200)
    subtitle = models.CharField(max_length =200,null=True)
    duration = models.CharField(max_length =200,null=True)
    content = models.CharField(max_length =2000,null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str___(self):
        return self.title
class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Blogsite,on_delete = models.CASCADE)
    text =  models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __string___(self):
        return f"{self.post.title}|{self.text[:30]}"    
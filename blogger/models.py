from django.db import models

# Create your models here.
class Blogsite(models.Model):
	title = models.CharField(max_length =200)
	body =models.TextField()
	date_publish = models.DateTimeField(auto_now_add=True)
	def __str___(self):
		return self.title
class Comment(models.Model):
	post = models.ForeignKey(Blogsite,on_delete = models.CASCADE)
	text = 	models.TextField()
	time = models.DateTimeField(auto_now_add=True)
	def __string___(self):
		return f"{self.post.title}|{self.text[:30]}"	
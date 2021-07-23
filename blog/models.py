from django.db import models

# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body_text = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
class Comments(models.Model)
    user = models.ForeignKey(User)
    post = models.ForeignKey(BlogPost)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
	comment = models.TextFied(default=None, blank=False, null=False)
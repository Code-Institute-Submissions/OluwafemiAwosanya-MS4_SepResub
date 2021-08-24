from django.db import models
from profiles.models import UserProfile


# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body_text = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title + '|' + str(self.user)
    
    
class Comments(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    comment = models.TextField(default=None, blank=False, null=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.comment + '|' + str(self.user)
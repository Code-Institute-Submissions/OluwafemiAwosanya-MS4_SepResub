from django.contrib import admin
from .models import BlogPost, Comments

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'created_at')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comments, CommentsAdmin)


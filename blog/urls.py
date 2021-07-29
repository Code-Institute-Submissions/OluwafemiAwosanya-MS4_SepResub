from django.urls import path
#from . import views
from .views import BlogView

urlpatterns = [
     path('', BlogView.as_view(), name="blog"),
    #path('', views.BlogPost, name='blog'),
]
from django.urls import path
from .views import blog_list, create_blog

urlpatterns = [
    path('pages/', blog_list, name='blog_list'),
    path("", create_blog, name="create_blog")
]

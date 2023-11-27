from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list') 
    else:
        form = BlogForm()

    return render(request, 'blog/create_blog.html', {'form': form})

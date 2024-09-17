from django.shortcuts import render, redirect,  get_object_or_404
from blogs.models import Blogs

def home(request):
    Blog = Blogs.objects.all()

    context = {
        'Blog' : Blog
    }
    return render(request, 'index.html', context)


def post(request, slug):
    blog = get_object_or_404(Blogs, new_slug=slug )
    context = {
        'blog': blog
    }

    return render(request, 'blog.html', context)
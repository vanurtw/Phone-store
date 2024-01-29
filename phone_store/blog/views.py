from django.shortcuts import render
from .models import Post, Categories


# Create your views here.
def blog_home(request):
    context = {'chapter': 'blog'}
    post = Post.objects.all()
    context['post'] = post

    return render(request, 'blog/blog.html', context)

from django.shortcuts import render
from .models import Post, Categories
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django.db.models import Q


# Create your views here.
def blog_home(request):
    context = {'chapter': 'blog'}
    if request.method == 'POST':
        search = request.POST.get('search')
        post = Post.objects.filter(Q(title__icontains=search) | Q(tags__name__icontains=search))
    else:
        category_slug = request.GET.get('category', None)

        if category_slug:
            category = Categories.objects.get(slug=category_slug)
            post = category.items.all()
        else:
            post = Post.objects.all()
    context['post'] = post

    return render(request, 'blog/blog.html', context)


def blog_details(request, slug):
    context = {'chapter':'blog'}
    post = get_object_or_404(Post, slug=slug)
    context['post'] = post
    return render(request, 'blog/blog-details.html', context)

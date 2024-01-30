from django.shortcuts import render
from .models import Post, Categories
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from .tasks import share_post
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
            tag_slug = request.GET.get('tag', None)
            if tag_slug:
                post = Post.objects.filter(tags__slug__in=[tag_slug])
            else:
                post = Post.objects.all()
    context['post'] = post

    return render(request, 'blog/blog.html', context)


def blog_details(request, slug):
    context = {'chapter': 'blog'}
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        email = request.POST.get('email')
        url_post = request.META['HTTP_REFERER']
        share_post.delay(email, url_post)
    context['post'] = post
    return render(request, 'blog/blog-details.html', context)

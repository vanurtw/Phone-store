from django.shortcuts import render
from .models import Post, Categories


# Create your views here.
def blog_home(request):
    context = {'chapter': 'blog'}
    if request.method == 'POST':
        search = request.POST.get('search')
        post = Post.objects.filter(title__icontains=search)
    else:
        category_slug = request.GET.get('category', None)
        if category_slug:
            category = Categories.objects.get(slug=category_slug)
            post = category.items.all()
        else:
            post = Post.objects.all()
    context['post'] = post

    return render(request, 'blog/blog.html', context)

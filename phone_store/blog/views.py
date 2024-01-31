from django.shortcuts import render, redirect
from .models import Post, Categories, Comment
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from .tasks import share_post
from django.db.models import Q


# Create your views here.
def blog_home(request):
    context = {'chapter': 'blog'}
    if request.method == 'POST':
        search = request.POST.get('search')
        post = Post.objects.filter(Q(title__icontains=search) | Q(tags__name__icontains=search)).distinct()
    else:
        category_slug = request.GET.get('category', None)
        if category_slug:
            context['category_slug'] = category_slug
            category = Categories.objects.get(slug=category_slug)

            post = category.items.all()
        else:
            tag_slug = request.GET.get('tag', None)
            if tag_slug:
                post = Post.objects.filter(tags__slug__in=[tag_slug])
                context['tag_slug'] = tag_slug
            else:
                post = Post.objects.all()
    context['post'] = post

    return render(request, 'blog/blog.html', context)


def blog_details(request, slug):
    context = {'chapter': 'blog'}
    post = get_object_or_404(Post, slug=slug)
    parent_id = request.GET.get('post_parent', None)
    parent = None
    if parent_id:
        parent = get_object_or_404(Comment, id=parent_id)
        context['parent'] = parent
    if request.method == 'POST':
        email = request.POST.get('email', None)
        if email:
            url_post = request.META['HTTP_REFERER']
            share_post.delay(email, url_post)
        else:
            post_id = request.POST.get('post')
            post = get_object_or_404(Post, id=post_id)
            user = request.user
            content = request.POST.get('content', None)
            Comment.objects.create(post=post, user=user, content=content, parent=parent)
            return redirect(to='blog_details', slug=slug)

    context['post'] = post
    context['comments'] = post.comments.all()
    return render(request, 'blog/blog-details.html', context)

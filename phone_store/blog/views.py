from django.shortcuts import render, redirect
from .models import Post, Categories, Comment
from django.shortcuts import get_object_or_404
from .tasks import share_post
from django.db.models import Q
from django.views.generic import View, DetailView


# Create your views here.
def blog_home(request):
    context = {'chapter': 'blog'}
    if request.method == 'POST':
        search = request.POST.get('search')
        post = Post.objects.filter(
            Q(title__icontains=search) | Q(tags__name__icontains=search)).distinct().select_related('category')
    else:
        category_slug = request.GET.get('category', None)
        if category_slug:
            context['category_slug'] = category_slug
            category = Categories.objects.get(slug=category_slug)
            post = category.items.all()
        else:
            tag_slug = request.GET.get('tag', None)
            if tag_slug:
                post = Post.objects.filter(tags__slug__in=[tag_slug]).select_related('category')
                context['tag_slug'] = tag_slug
            else:
                post = Post.objects.all().select_related('category')
    context['post'] = post
    return render(request, 'blog/blog.html', context)


class BlogPostDetail(DetailView):
    template_name = 'blog/blog-details.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return Post.objects.get(slug=slug)

    def get_context_data(self, **kwargs):
        context = super(BlogPostDetail, self).get_context_data(**kwargs)
        context['chapter'] = 'blog'
        context['parent'] = None
        request = self.request
        parent_id = request.GET.get('post_parent', None)
        if parent_id:
            context['parent'] = Comment.objects.filter(id=parent_id).select_related('user').first()
        context['comments'] = context['post'].comments.all().select_related('user', 'parent')
        return context


def blog_details(request, slug):
    context = {'chapter': 'blog'}
    post = Post.objects.get(slug=slug)
    parent_id = request.GET.get('post_parent', None)
    parent = None
    if parent_id:
        parent = Comment.objects.filter(id=parent_id).select_related('user').first()

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
    context['comments'] = post.comments.all().select_related('user', 'parent')
    # context['comments']  = Comment.objects.filter(post=post).select_related('user', 'parent')
    return render(request, 'blog/blog-details.html', context)

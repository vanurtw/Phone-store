from django import template
from blog.models import Categories, Post
from taggit.models import Tag
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('categories.html', name='categories')
def category():
    categories = Categories.objects.all()
    return {'categories': categories}


@register.inclusion_tag('popular_post.html', name='popular_post')
def popular_post():
    post = Post.objects.filter(popular=True)
    return {'post': post}


@register.inclusion_tag('tags.html', name='tags')
def tags():
    tags = Tag.objects.all()
    return {'tags': tags}


@register.simple_tag(name='next_post')
def next_post(post):
    try:
        post_next = Post.objects.get(id=post.id + 1)
    except ObjectDoesNotExist:
        post_next = Post.objects.all().first()
    return post_next


@register.simple_tag(name='prev_post')
def prev_post(post):
    try:
        post_prev = Post.objects.get(id=post.id - 1)
    except ObjectDoesNotExist:
        post_prev = Post.objects.all().last()
    return post_prev

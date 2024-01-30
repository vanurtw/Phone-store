from django import template
from blog.models import Categories, Post
from taggit.models import Tag

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

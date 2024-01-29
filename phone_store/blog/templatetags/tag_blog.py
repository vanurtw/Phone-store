from django import template
from blog.models import Categories

register = template.Library()


@register.inclusion_tag('categories.html', name='categories')
def category():
    categories = Categories.objects.all()
    return {'categories': categories}

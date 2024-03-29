from django import template

register = template.Library()


@register.filter(name='distinct')
def distinct(qs, param):
    dic_queryset = {}
    queryset = []
    for item in qs:
        atribute = getattr(item, param)
        if atribute not in dic_queryset:
            queryset.append(item)
            dic_queryset[atribute] = True
    return queryset


@register.inclusion_tag('product_header.html', takes_context=True)
def product_header(context):
    return {'prod_header': context['prod_header'], 'product': context['product'],
            'comment_count': context['comment_count']}


@register.inclusion_tag('product_header_content.html', takes_context=True)
def product_header_content(context):
    prod_com = context['product'].comments.all().select_related('user')
    return {'prod_header': context['prod_header'], 'product': context['product'],
            'comment_count': context['comment_count'], 'prod_com': prod_com,
            'color_product': context['color_product'], 'form': context['form'], 'user': context['user']}


@register.filter(name='range')
def range_filter(count):
    if not count:
        count = 5
    return [i for i in range(int(count))]


@register.filter(name='range_none')
def range_filter_none(count):
    if not count:
        count = 5
    return [i for i in range(int(count), 5)]

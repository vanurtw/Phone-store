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
    return {'prod_header': context['prod_header']}


@register.inclusion_tag('product_header_content.html', takes_context=True)
def product_header_content(context):
    return {'prod_header': context['prod_header'], 'product': context['product'],
            'color_product': context['color_product']}

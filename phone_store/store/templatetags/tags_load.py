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


@register.inclusion_tag('product_header.html')
def product_header(header):
    return {'prod_header':header}

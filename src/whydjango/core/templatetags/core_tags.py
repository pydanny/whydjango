from django import template
from django.contrib.flatpages.models import FlatPage

from whydjango.core.models import TopLink

register = template.Library()

@register.inclusion_tag('core/top_link.html')
def top_links():
    return { 'links':TopLink.objects.all() }
    
@register.simple_tag
def breadcrumbs(flatpage):
    absolute_url = flatpage.get_absolute_url()
    text = ''
    url = ''
    elements = absolute_url[1:-1].split('/')
    length = len(elements) - 1
    if length < 1:
        return ''
    for i, element in enumerate(elements):
        url += '/%s' % element
        flatpage = FlatPage.objects.get(url='%s/' % url)
        if length == i:
            text += flatpage.title
            break
        text += '<a href="%s/">%s</a> ' % (url, flatpage.title)

    return text

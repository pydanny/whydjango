from django import template

from whydjango.core.models import TopLink

register = template.Library()

@register.inclusion_tag('core/top_link.html')
def top_links():
    return { 'links':TopLink.objects.all() }
    
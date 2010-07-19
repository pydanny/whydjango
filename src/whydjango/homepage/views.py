from django.shortcuts import render_to_response
from django.template import RequestContext

from whydjango.homepage.models import Content

def homepage(request, template_name='homepage/index.html'):
    
    return render_to_response(
        template_name, {
            'css_items':    Content.objects.css(),
            'js_items':     Content.objects.js(),
            'html_items':   Content.objects.html(),            
        }, context_instance=RequestContext(request)
    )

from django.conf.urls.defaults import * 

from django.views.generic.list_detail import object_list, object_detail

from whydjango.casestudies.models import CaseStudy

urlpatterns = patterns('',

    url(
        regex = '(?P<slug>[-\w]+)/',
        view    = object_detail, 
        name = 'case_study',
        kwargs=dict(
            queryset=CaseStudy.objects.all(),
            template_name='casestudies/casestudy.html',
            )        
    ),

    url(
        regex = '^$',
        view    = object_list, 
        name = 'casestudies',
        kwargs=dict(
            queryset=CaseStudy.objects.all(),
            template_name='casestudies/index.html',
            )        
    ),

)
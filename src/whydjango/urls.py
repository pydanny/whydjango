from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from whydjango.casestudies.views import case_study_submission

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^books/', include('whydjango.books.urls')),    
    (r'^case-studies/', include('whydjango.casestudies.urls')),
    url(
        regex = "submit-proposal/",
        view  = case_study_submission,
        name = "case_study_submission"
    )    
)

# Debug settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )



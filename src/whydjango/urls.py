from django.conf.urls.defaults import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    
    (r'^casestudies/', include('whydjango.casestudies.urls')),
    (r'^/', include('whydjango.homepage.urls')), 
)

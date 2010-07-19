from django.conf.urls.defaults import * 

from whydjango.homepage.views import homepage

urlpatterns = patterns('',

    url(
        regex   = '',
        view    = homepage, 
        name    = 'homepage',
    ),

)
from django.conf.urls.defaults import * 

from django.views.generic.list_detail import object_list, object_detail

from whydjango.books.models import Book

urlpatterns = patterns('',

    url(
        regex = '^$',
        view    = object_list, 
        name = 'books',
        kwargs=dict(
            queryset=Book.objects.all(),
            template_name='books/index.html',
            )        
    ),

)
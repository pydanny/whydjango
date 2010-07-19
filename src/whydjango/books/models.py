from django.db import models
from django.utils.translation import ugettext_lazy as _ 

from whydjango.models import StandardModel

class Book(StandardModel):
    
    title           = models.CharField(_('Title'), max_length=100)
    authors         = models.CharField(_('Title'), max_length=255)
    book_type       = models.CharField(_('Book Type'), max_length=100)
    length          = models.IntegerField(_('Book Length'))
    release_date    = models.CharField(_('Release Date'), max_length=50)
    language        = models.CharField(_('Language'), max_length=50)
    ISBN            = models.CharField(_('ISBN'), max_length=50)
    ISBN_13         = models.CharField(_('ISBN-13'), max_length=50)
    available       = models.BooleanField(_('Available')
    #thumbnail       = ???
    
class BookOrderLinks(StandardModel):
    
    book            = models.ForeignKey(Book, related='book_order_link')
    link            = models.URLField(_('link'))
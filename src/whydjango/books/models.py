from django.db import models
from django.utils.translation import ugettext_lazy as _ 

from taggit.managers import TaggableManager

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
    image           = models.ImageField(_('Image'), upload_to='book_images')
    
    tags            = TaggableManager()    
    
    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
        
    def __unicode(self):
        return self.title
    
class BookOrderLinks(StandardModel):
    
    book            = models.ForeignKey(Book, related='book_order_link')
    link            = models.URLField(_('link'))
    
    verbose_name = _('Entry Image')
    verbose_name_plural = _('Entry Images')
    
    def __unicode(self):
        return self.title
    
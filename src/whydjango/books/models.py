from django.db import models
from django.utils.translation import ugettext_lazy as _ 

from taggit.managers import TaggableManager

from whydjango.models import StandardModel

BOOK_TYPE_CHOICES =(
    ('Paperback', 'Paperback'),
    ('Hardback', 'Hardback'),
    ('eBook', 'eBook'),
)

class Book(StandardModel):
    
    title           = models.CharField(_('Title'), max_length=255)
    authors         = models.CharField(_('Authors'), max_length=255)
    book_type       = models.CharField(_('Book Type'), max_length=100, choices=BOOK_TYPE_CHOICES)
    length          = models.IntegerField(_('Book Length'), help_text="length in pages")
    release_date    = models.DateField(_('Release Date'), blank=True, help_text="Only the month and year will be displayed")
    language        = models.CharField(_('Language'), max_length=50)
    ISBN            = models.CharField(_('ISBN'), max_length=50)
    ISBN_13         = models.CharField(_('ISBN-13'), max_length=50)
    available       = models.BooleanField(_('Available'))
    image           = models.ImageField(_('Image'), upload_to='book_images')
    
    tags            = TaggableManager()  
    
    class Meta:
        ordering = ('-release_date', '-available')
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
        
    def __unicode__(self):
        return self.title
        
    def get_first_order_link(self):
        try:
            return self.book_order_link.all()[0]
        except IndexError:
            return None
    
class BookOrderLink(StandardModel):
    
    book            = models.ForeignKey(Book, related_name='book_order_link')
    publisher       = models.CharField(_('Publisher'), max_length=100)
    link            = models.URLField(_('link'))
    
    class Meta:
        ordering = ('-id',)
        verbose_name = _('Book Order Link')
        verbose_name_plural = _('Book Order Links')
    
    def __unicode__(self):
        return 'Link for: "%s"' % self.book.__unicode__()
    
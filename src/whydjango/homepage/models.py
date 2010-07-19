import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _ 

from django_extensions.db.fields import AutoSlugField

from whydjango.models import StandardModel

ELEMENT_TYPE = (
        ('css', 'CSS'),
        ('js', 'JavaScript'),        
        ('html', 'HTML'),
    )
        
class ContentManager(models.Manager):
    
    def css(self):
        return super(ContentManager, self).get_query_set().filter(element_type='css')        

    def js(self):
        return super(ContentManager, self).get_query_set().filter(element_type='js')        

    def html(self):
        return super(ContentManager, self).get_query_set().filter(element_type='html')        

class Content(StandardModel):
    
    title           = models.CharField(_('Title'), max_length=100, blank=True, default='')
    element_type    = models.CharField(_('Element Type'), choices=ELEMENT_TYPE, max_length=100)
    order           = models.IntegerField(_('order'))        
    content         = models.TextField(_('Content'), blank=True, default='')
    
    objects = ContentManager()
    
    class Meta:
        ordering = ('order',)    
    
    def __unicode__(self):
        return self.title
    
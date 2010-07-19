from django.db import models
from django.utils.translation import ugettext_lazy as _ 

from django_extensions.db.fields import AutoSlugField

from whydjango.models import StandardModel

class TopLink(StandardModel):
    
    title       = models.CharField(_('Title'), max_length=100)
    slug        = AutoSlugField(_('Slug'), populate_from='title')
    description = models.TextField(_('Description'), blank=True, default='')
    order       = models.IntegerField(_('order'))
    
    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.title
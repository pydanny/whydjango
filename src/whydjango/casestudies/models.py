import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _ 

from django_extensions.db.fields import AutoSlugField
from taggit.managers import TaggableManager

from whydjango.models import StandardModel

class BaseModel(StandardModel):
    title           = models.CharField(_('title'), max_length=50)
    description     = models.TextField(_('description'), blank=True)
    slug            = AutoSlugField(_('Slug'), populate_from='title')
    
    class Meta:
        abstract = True
        
    def __unicode__(self): 
        return self.slug
        

class CaseStudy(BaseModel):
    url = models.URLField(_('url'), blank=True, default='')
    tags = models.CharField(max_length=100)
    authors = models.ManyToManyField(User)
    content = models.TextField(_('content')) 
    pub_date = models.DateTimeField(_('date posted'), default=datetime.datetime.today)

    tags            = TaggableManager()
    
    @models.permalink
    def get_absolute_url(self):
        return ('case_study', (), {'slug': self.slug})

    class Meta:
        get_latest_by = 'title'
        ordering = ['title']        
        verbose_name = _('Case Study')
        verbose_name_plural = _('Case Studies')
        
class CaseStudyImage(BaseModel):

    case_study = models.ForeignKey(CaseStudy, related_name='case_study_image')
    image = models.ImageField(_('Image'), upload_to='case_study_images/%Y/%m/%d')

    class Meta:
        verbose_name = _('Case Study Image')
        verbose_name_plural = _('Case Study Images')

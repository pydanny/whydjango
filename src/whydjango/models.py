from django.db import models 
import datetime 
from django.utils.translation import ugettext_lazy as _ 

from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField 

class StandardModel(models.Model): 
    """ StandardModel abstract base class to give creation and modified times """
    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    class Meta: 
        abstract = True 

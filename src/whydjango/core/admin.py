from django.contrib import admin 

from whydjango.core.models import TopLink


class TopLinkAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(TopLink, TopLinkAdmin)

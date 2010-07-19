from django.contrib import admin 

from whydjango.homepage.models import TopLink, Content


class TopLinkAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(TopLink, TopLinkAdmin)

class ContentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Content, ContentAdmin)
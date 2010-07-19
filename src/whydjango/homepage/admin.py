from django.contrib import admin 

from whydjango.homepage.models import Content



class ContentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Content, ContentAdmin)
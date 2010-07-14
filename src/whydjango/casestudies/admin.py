from django.contrib import admin 

from whydjango.casestudies.models import CaseStudy, CaseStudyImage


class CaseStudyAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(CaseStudy, CaseStudyAdmin)

class CaseStudyImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(CaseStudyImage, CaseStudyImageAdmin)
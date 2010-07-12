from django.contrib import admin 

from whydjango.case_studies.models import CaseStudy, CaseStudyImage


class CaseStudyAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(CaseStudy, CaseStudyAdmin)

class CaseStudyImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(CaseStudyImage, CaseStudyImageAdmin)
from django.contrib import admin 

from whydjango.casestudies.models import CaseStudy, CaseStudyImage, CaseStudySubmission


admin.site.register(CaseStudy)
admin.site.register(CaseStudyImage)
admin.site.register(CaseStudySubmission)
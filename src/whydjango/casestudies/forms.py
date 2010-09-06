from django import forms

from whydjango.casestudies.models import CaseStudySubmission

class SubmitCaseStudyForm(forms.ModelForm):
     
     class Meta:
         
         model = CaseStudySubmission
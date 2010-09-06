from django.core.urlresolvers import reverse 
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template import RequestContext 


from whydjango.casestudies.forms import SubmitCaseStudyForm

def case_study_submission(request, template_name="casestudies/submit.html"):

        form = SubmitCaseStudyForm(request.POST or None)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("case_study_submission"))

        return render_to_response(template_name, { 
            "form": form,
            }, context_instance=RequestContext(request))    
    
    
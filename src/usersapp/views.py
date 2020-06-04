from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import IncidentForm
from .models import Incident
from django.views.decorators.http import require_POST

# Create your views here.
# add a new view function called incident_create
def  home (request): 
    #incident = Incident.objects.get(pk=1)
    return render(request,'index.html')

def incident_create(request):
    if request.method == 'POST':
        
        #form = IncidentForm(request.POST)
        userform = IncidentForm(request.POST)

        #if form.is_valid():
        if userform.is_valid():

            #form.save()
            userform.save()
            
            print('form submitted')
            messages.info(request, 'Thank you for reporting')
            return redirect('incident_create')
    else:
        print('Unable to submit')
        messages.info(request, 'Unable to submit, some fields cannot be empty')

        #form = IncidentForm()
        userform = IncidentForm()
    
    return render(request,
    'incident_create.html',
    {
        #'form': form
        'form': userform
    })

def responder(request):
    detail=Incident.objects.all()
    return render(request,
    'responder.html',
    {
        'detail': detail
    })
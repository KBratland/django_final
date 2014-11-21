from django.views.generic import ListView
from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
import json

from .forms import PersonForm
from .models import Person

# Create your views here

@login_required
def person_profile(request):

    if request.method == "POST":
        form = PersonForm(request.POST, instance=request.user.profile)
        if form.is_valid:
            form.save()
# TODO create a landing page for logged in users - or could redirect them to the ethics and picking sections? - could do JS replace of objects in the DOM to be links for find and add - or could do if statement on html for alternate extends
            return HttpResponseRedirect('/', {'first_name': request.user.username})
    else:
        user = request.user
        profile = user.profile
        form = PersonForm(instance=profile)

    token = {}
    token.update(csrf(request))
    token['form'] = form

    current_user = Person.objects.get(user_id=request.user.profile.user_id)
    username = request.user.username
    first_name = current_user.first_name
    token['first_name'] = first_name
    token['username'] = username

    return render_to_response('person_profile.html', token)




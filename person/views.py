from django.views.generic import ListView
from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User

from .forms import PersonForm

# Create your views here

@login_required
def person_profile(request):

    if request.method == "POST":
        form = PersonForm(request.POST, instance=request.user.profile)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/login_success/')
    else:
        user = request.user
        profile = user.profile
        form = PersonForm(instance=profile)

    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('person_profile.html', token)


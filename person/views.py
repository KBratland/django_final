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
            return HttpResponseRedirect('/login_success/')
    else:
        user = request.user
        profile = user.profile
        form = PersonForm(instance=profile)

    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('person_profile.html', token)


def api_endpoint(request):
    item_list = Person.Objects.all()
    output_list = []

    for item in item_list:
        output_item = {}
        output_item["system_id"] = item.id
        output_item["first_name"] = item.first_name
        output_item["last_name"] = item.last_name
        output_list.append(output_item)

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )

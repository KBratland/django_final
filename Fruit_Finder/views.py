__author__ = 'Kristin'

from django.contrib.auth.models import User
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from .forms import RegistrationForm

#Registration functions


def home(request):
    return render_to_response('Fruit_Finder_base.html')


def registration(request):
    form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('registration_success.html')
            # username = request.POST.get('username', '')
            # password = request.POST.get('password', '')
            # user = auth.authenticate(username=username, password=password)
            #
            # if user is not None:
            #     if user.is_active:
            #         auth.login(request, user)
            #
            # return render_to_response('profile.html', {'first_name':request.user.username})

    return render_to_response('registration.html', token)


# def registration_success():
#     username = User.objects.get()
#     return render_to_response('registration_success.html', {'username':username})


# def registration_success():
# #     return HttpResponseRedirect('person/',)
#
#
# def password_reset():
#
# #Log-in functions
#
# def login():
#
# def authentication():
# username = request.POST.get('username', '')
# password = request.POST.get('password', '')
# user = auth.authenticate(username=username, passowrd=password)
#
# if user is not None:

#
# def login_success():
#
# def login_fail():
#
# def logout():
#
# def invalid_user():

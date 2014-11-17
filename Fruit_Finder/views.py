__author__ = 'Kristin'
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from .forms import RegistrationForm

#Registration functions


def home(request):
    return render_to_response('Fruit_Finder_base.html')


def registration(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('registration_success.html')

        else:
            return render_to_response('registration_fail.html')

    else:
        form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration.html', token)


#Log-in functions
def login(request):
    token = {}
    token.update(csrf(request))
    return render_to_response('login.html', token)


def authenticate(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/login_success')
    else:
        return HttpResponseRedirect('/invalid')


def login_success(request):
    return render_to_response('login_success.html', {'first_name': request.user.username})


def invalid(request):
    return render_to_response('invalid.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')



#      username = request.POST.get('username', '')
#             password = request.POST.get('password', '')
#             user = auth.authenticate(username=username, password=password)
#
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#
#             return render_to_response('profile.html', {'first_name':request.user.username})

__author__ = 'kristin'

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views  import generic


# from person.views import PersonProfile

urlpatterns = patterns('',
    url(r'^$', 'person.views.person_profile', name="person_profile"),
    )
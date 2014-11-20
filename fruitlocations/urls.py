__author__ = 'kristin'

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views  import generic
from fruitlocations import views


# from person.views import PersonProfile

urlpatterns = patterns('',
    url(r'^add_fruit/$', views.add_fruit, name="add_fruit"),
    url(r'^find_fruit/$', views.find_fruit, name="find_fruit")

    )
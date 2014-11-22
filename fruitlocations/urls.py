__author__ = 'kristin'

from django.conf.urls import patterns, url

from fruitlocations import views


# from person.views import PersonProfile

urlpatterns = patterns('',
    url(r'^add_fruit/$', views.add_fruit, name="add_fruit"),
    url(r'^find_fruit/$', views.find_fruit, name="find_fruit"),
    url(r'^ajax_get_fruit/$', views.ajax_get_fruit, name="ajax_get_fruit"),
    )
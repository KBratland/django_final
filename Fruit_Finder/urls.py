from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Home:
    url(r'^$', 'Fruit_Finder.views.home', name='home'),

    #avatar url
    #url(r'^avatar/', include('avatar.urls')),

    #urls for registration
    url(r'^registration/$', 'Fruit_Finder.views.registration', name='registration'),


    #urls for login/logout/authentication/invalid_user
    url(r'^login/$', 'Fruit_Finder.views.login', name='login'),
    url(r'^login_success/$', 'Fruit_Finder.views.login_success', name='login_success'),
    url(r'^authenticate/$', 'Fruit_Finder.views.authenticate', name='authenticate'),
    url(r'^invalid/$', 'Fruit_Finder.views.invalid', name='invalid'),
    url(r'^logout/$', 'Fruit_Finder.views.logout', name='logout'),
    url(r'^ethics/$', 'Fruit_Finder.views.ethics', name='ethics'),
    url(r'^pick/$', 'Fruit_Finder.views.pick', name='pick'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^person/', include('person.urls')),
    url(r'^fruitlocations/', include('fruitlocations.urls')),
)

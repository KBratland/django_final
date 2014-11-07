from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Home:
    url(r'^$', 'Fruit_Finder.views.home', name='home'),

    #somehow I need to load both .registration and .login

    #avater url
    #url(r'^avatar/', include('avatar.urls')),

    #urls for registration

    url(r'^registration/$', 'Fruit_Finder.views.registration', name='registration'),
    # url(r'^password_reset/$', 'Fruit_Finder.views.password_reset', name='password_reset'),

    #urls for login/logout/authentication/invalid_user
    url(r'^login/$', 'Fruit_Finder.views.login', name='login'),
    url(r'^login_success/$', 'Fruit_Finder.views.login_success', name='login_success'),
    url(r'^authenticate/$', 'Fruit_Finder.views.authenticate', name='authenticate'),
    url(r'^invalid/$', 'Fruit_Finder.views.invalid', name='invalid'),

    # url(r'^logout/$', 'Fruit_Finder.views.logout', name='register'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^person/', include('person.urls')),

)

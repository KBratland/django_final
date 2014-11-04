from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Home:
    url(r'^$', 'Fruit_Finder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'signups.views.home', name='home'),

    #urls for registration
    url(r'^registration/$', 'Fruit_Finder.views.registration', name='registration'),
    # url(r'^registration_success/$', 'Fruit_Finder.views.registration_success', name='registration_success'),
    # url(r'^registration_fail/$', 'Fruit_Finder.views.registration_fail', name='registration_fail'),
    # url(r'^password_reset/$', 'Fruit_Finder.views.password_reset', name='password_reset'),

    #urls for login/logout/authentication/invalid_user
    # url(r'^login/$', 'Fruit_Finder.views.login', name='register'),
    # url(r'^login_success/$', 'Fruit_Finder.views.login_success', name='login_success'),
    # url(r'^authentication/$', 'Fruit_Finder.views.authentication', name='register'),
    # url(r'^logout/$', 'Fruit_Finder.views.logout', name='register'),
    # url(r'^logout_success/$', 'Fruit_Finder.views.logout_success', name='logout_success'),
    # url(r'^invalid_user/$', 'Fruit_Finder.views.invalid_user', name='invalid_user'),

    url(r'^admin/', include(admin.site.urls)),

)

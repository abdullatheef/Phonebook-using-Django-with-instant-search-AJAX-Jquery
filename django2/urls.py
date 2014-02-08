from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from phonebook.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    url(r'^check$', check),
    url(r'^signup$', signup),
    url(r'^addperson$', add),
    url(r'^addcontact$', addc),
    url(r'^logout$', logout),
    url(r'^instant$', instant),
    url(r'^admin/', include(admin.site.urls)),
)
from django.conf import settings
urlpatterns += patterns('', (r'^static/(.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT }), )  

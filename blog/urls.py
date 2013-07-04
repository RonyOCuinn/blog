from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'RehabLog.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'RehabLog.views.post'),
)

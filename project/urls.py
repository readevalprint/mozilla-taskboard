from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include
from funfactory.monkeypatches import patch

patch()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('project.taskboard.urls')),
    (r'^browserid/', include('django_browserid.urls')),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL,
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

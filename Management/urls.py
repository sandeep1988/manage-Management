from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from ProManagement.views import foo
import polls
urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^polls/', include('polls.urls', namespace='polls', app_name='polls')),
    url(r'ProManagement/$', foo),
    url(r'^$', foo, name='home')
	#url(r'^places/(?P<name>\w+)/$', 'misc.views.home', name='places.view_place')
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

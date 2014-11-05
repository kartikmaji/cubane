from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cubane.views.home', name='home'),
    url(r'^signup', 'cubane.views.signup', name='signup'),
    url(r'^login', 'cubane.views.user_login', name='user_login'),
    url(r'^newchannel', 'cubane.views.newchannel', name='newchannel'),
    url(r'^(?P<channel_id>[0-9]+)/$', 'cubane.views.showchannel', name='showchannel'),
    url(r'^(?P<channel_id>[0-9]+)/join$', 'cubane.views.joinchannel', name='joinchannel'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


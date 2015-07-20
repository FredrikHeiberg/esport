from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'register.views.home', name='home'),
    url(r'^headset/$', 'register.views.headset', name='headset'),
    # url(r'^blog/', include('blog.urls')),
)

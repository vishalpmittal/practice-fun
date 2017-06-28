from django.conf.urls import patterns, include, url

from django.contrib import admin

from .views import HelloWorldView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HelloWorldView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

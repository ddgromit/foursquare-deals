from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('core.views',
    url('^/?','homepage_handler'),
)

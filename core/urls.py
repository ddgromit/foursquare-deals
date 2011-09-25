from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('core.views',
    url('^$','homepage_handler'),
    url('^login$','foursquare_login_handler'),
    url('^callback$','foursquare_login_callback'),
    url('^logout$','logout_handler'),
)

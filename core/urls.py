from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('core.views',
    url('^$','homepage_handler'),
    url('^login$','foursquare_login_handler'),
    url('^callback$','foursquare_login_callback'),
    url('^update_notifo','update_notifo_handler'),
    url('^test_notifo','test_notifo_handler'),
    url('^update_boxcar','update_boxcar_handler'),
    url('^logout$','logout_handler'),
)

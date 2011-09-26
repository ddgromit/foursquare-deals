from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('core.views',
    url('^$','homepage_handler'),

    # Auth
    url('^login$','foursquare_login_handler'),
    url('^logout$','logout_handler'),
    url('^callback$','foursquare_login_callback'),

    # User account form
    url('^update_notifo$','update_notifo_handler'),
    url('^test_notifo$','test_notifo_handler'),
    url('^update_boxcar$','update_boxcar_handler'),

    # Homepages
    url('^checkin_offers$','checkin_offers_handler'),

    # Foursquare API
    url('^checkin_push$','checkin_push_handler'),

)

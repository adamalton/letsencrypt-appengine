from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    'letsencryptae.views',
    url(r'^\.well-known/acme-challenge/(?P<url_slug>[a-zA-z0-9_-]+)$', 'secret', name='secret'),
)

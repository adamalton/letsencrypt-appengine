# THIRD PARTY
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# LETS ENCRYPT APP ENGINE
from letsencryptae.models import Secret


def secret(request, url_slug):
    """ Serves the secret that Let's Encrypt requires us to serve in order to validate that we own
        the domain.
    """
    secret = get_object_or_404(Secret, url_slug=url_slug)
    return HttpResponse(secret.secret)

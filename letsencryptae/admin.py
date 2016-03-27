# THIRD PARTY
from django.contrib import admin

# LETS ENCRYPT APP ENGINE
from letsencryptae.models import Secret

admin.site.register(Secret)

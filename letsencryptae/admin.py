# THIRD PARTY
from django.contrib import admin

# LETS ENCRYPT APP ENGINE
from letsencryptae.models import Secret


class SecretAdmin(admin.ModelAdmin):
    list_display = ('url_slug', 'created')


admin.site.register(Secret, SecretAdmin)

# THIRD PARTY
from djangae.fields import CharField
from django.db import models


class Secret(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url_slug = CharField(primary_key=True)
    secret = CharField()

    def __unicode__(self):
        return self.url_slug

    def clean(self, *args, **kwargs):
        return_value = super(Secret, self).clean(*args, **kwargs)
        if not self.secret.startswith(self.url_slug):
            raise ValidationError("The URL slug and the beginning of the secret should be the same.")

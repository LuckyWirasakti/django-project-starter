from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from core.mixins import TimeStampModelMixins

# Create your models here.
class Listener(TimeStampModelMixins):
    url = models.TextField(help_text="https://example.com/api/v1/webhook")
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "listener"
        verbose_name_plural = "listeners"

    def __str__(self):
        return self.url
    
    def get_url(self):
        return mark_safe('<a href="{}" target="_blank">{}</a>'.format(self.url, self.url))
    get_url.short_description = 'url'
from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User

# Create your models here.
class Gallery(models.Model):
    file = models.FileField(upload_to='gallery', max_length=100)
    caption = models.TextField()
    content_type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "gallery"
        verbose_name_plural = "galleries"

    def __str__(self):
        return self.caption

    def get_file(self):
        content_type = self.content_type.split('/')[0]
        if content_type == "image":
            return mark_safe('<img src="/media/%s" width="250" />' % (self.file))
        if content_type == "video":
            return mark_safe('<video width="250" controls><source src="/media/%s" type="%s">Your browser does not support the video tag.</video>' % (self.file, self.content_type))
    get_file.short_description = "file"

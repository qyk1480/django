from django.db import models
from tinymce.models import HTMLField


class AreaInfo(models.Model):
    title = models.CharField(max_length=10)
    parea = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


class Tinymce1(models.Model):
    content = HTMLField()

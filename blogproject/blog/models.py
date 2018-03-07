from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags
# Create your models here.

@python_2_unicode_compatible
class meta(models.Model):
    metabolomics = models.CharField(max_length = 200)
    mz = models.FloatField()
    rt = models.FloatField()
    provider = models.ForeignKey(User)
    updatetime = models.DateTimeField()
    def __str__(self):
        return self.metabolomics
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models

class meta(models.Model):
    metabolomics = models.CharField(max_length = 200)
    mz = models.FloatField()
    rt = models.FloatField()
    user = models.ForeignKey(User)
    updatetime = models.DateTimeField
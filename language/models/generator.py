
from django.contrib.auth.models import User
from django.db import models

class Generator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    repeat = models.SmallIntegerField()
    translate_repeat = models.SmallIntegerField()
    random = models.BooleanField()


    def __unicode__(self):
        return self.name
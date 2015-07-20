from django.db import models

# Create your models here.
class Join(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=False)
    last_name = models.CharField(max_length=120, null=True, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    address = models.CharField(max_length=120, null=True, blank=False)
    zipcode = models.CharField(max_length=4, null=True, blank=False)
    area = models.CharField(max_length=100, null=True, blank=False)
    ref_id = models.CharField(max_length=120, default='default', unique=True)
    password = models.CharField(max_length=120, null=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return str(self.email)

    class META:
        unique_together = ('email', 'ref_id',)

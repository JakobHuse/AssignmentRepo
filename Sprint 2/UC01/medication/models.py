from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your models here.
class patient_medication(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=10)
    description = models.CharField(max_length=1000)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='medications')

    def __str__(self):
        return self.name
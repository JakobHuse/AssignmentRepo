from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your models here.
class patient_medication(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=10)
    description = models.CharField(max_length=1000)

    #define choices
    DAILY = "Daily"
    WEEKLY = "Weekly"
    OTHER = "Other"

    FREQUENCY_CHOICES = {
        DAILY: "Daily",
        WEEKLY: "Weekly",
        OTHER: "Other"
    }
    
    frequency = models.CharField(
        max_length=6,
        choices=FREQUENCY_CHOICES,
        default=DAILY,
    )

    EMAIL = "Email"
    TEXT = "Text"
    CALL = "Call"

    REMINDER_CHOICES = {
        EMAIL: "Email",
        TEXT: "Text",
        CALL: "Call",
    }
    
    reminder_type = models.CharField(
        max_length=5,
        choices=REMINDER_CHOICES,
        default=EMAIL,
    )



    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='medications')

    def __str__(self):
        return self.name
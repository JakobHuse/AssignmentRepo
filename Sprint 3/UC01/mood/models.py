from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import date


# Create your models here.
class mood_entry(models.Model):
    date = models.DateField(default=date.today)
    description = models.CharField(max_length=1000)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='moods')
    
    def __str__(self):
        # Format the event_date as 'YYYY-MM-DD'
        return self.date.strftime('%Y-%m-%d')
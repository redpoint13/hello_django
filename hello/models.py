from django.db import models
from django.utils import timezone

"""
The general workflow is as follows:

1 - Make changes to the models in your models.py file.
2 - Run python manage.py makemigrations to generate scripts in the migrations folder that migrate the database from its current state to the new state.
3 - Run python manage.py migrate to apply the scripts to the actual database.
"""


# Create your models here.

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

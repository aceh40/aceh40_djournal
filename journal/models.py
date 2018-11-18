from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.


class JournalEntry(models.Model):
    """ Used to store entries made by user.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(blank=True, default=timezone.now())

    def __str__(self):
        return f'Title: {self.title}, date: {self.created_date}'

    def publish(self):
        self.created_date = timezone.now()
        self.save()
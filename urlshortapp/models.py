
from django.db import models
from django.utils import timezone
from .utils import create_shortened_url

class Shortener(models.Model):

    created = models.DateTimeField()
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url} created on {self.created} times_followed {self.times_followed}'

    def save(self, *args, **kwargs):
        if not self.short_url:

            self.short_url = create_shortened_url(self)
            self.created = timezone.now()

        super().save(*args, **kwargs)

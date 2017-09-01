from django.db import models

class Attachment(models.Model):
    name = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-upload_date"]

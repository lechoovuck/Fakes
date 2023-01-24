from django.db import models

class MalwareSite(models.Model):
    url = models.CharField(max_length=80, blank = True, null = True)
    def __str__(self):
        return self.url

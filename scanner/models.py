from django.db import models

class MalwareSite(models.Model):
    url = models.URLField(max_length=120,help_text="Please use the following format http://example.com or https://example.com")
    def __str__(self):
        return self.url

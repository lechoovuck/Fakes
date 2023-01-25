import json
from django.db import models
from django.utils import timezone

class ScrapyItem(models.Model):
    start_url = models.URLField(max_length=120,help_text="Please use the following format http://example.com or https://example.com")
    unique_id = models.CharField(max_length=100, null=True)
    data = models.TextField() 
    date = models.DateTimeField(default=timezone.now)
    
    @property
    def to_dict(self):
        data = {
            'start url': self.start_url,
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    def __str__(self):
        return self.unique_id
    
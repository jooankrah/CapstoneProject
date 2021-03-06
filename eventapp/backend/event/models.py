from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length= 100)
    location = models.CharField(max_length= 100)
    morning = 'Morning'
    midmorning = 'Midmorning'
    afternoon = 'Afternoon'
    EVENT_TIME_CHOICES = [
        (morning, 'Morning'),
        (midmorning, 'Midmorning'),
        (afternoon, 'Afternoon'),
    ]
    event_time = models.CharField(max_length=15, choices=EVENT_TIME_CHOICES)
    speaker = models.CharField(max_length= 100)
    topic = models.CharField(max_length=300)
    roomcapacity = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'uploads/')



    def __str__(self):
        return self.title
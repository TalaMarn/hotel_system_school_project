from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    ROOM_TYPE = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Family', 'Family'),
    ]
    roomNo = models.CharField(max_length=10)
    roomType = models.CharField(max_length=10, choices=ROOM_TYPE, default='Single')
    price = models.FloatField()
    roomPic = models.ImageField(upload_to='Room_Img/', null=True, blank=True)
    isAvailable = models.BooleanField(default=True)
    
    def __str__(self):
        return self.roomNo
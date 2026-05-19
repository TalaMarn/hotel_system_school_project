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
    
class Booking(models.Model):

    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    customer_name = models.CharField(max_length=100)

    email = models.EmailField()

    check_in = models.DateField()

    check_out = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)



class Profile(models.Model):
    Role_CHOICES = [
        ('Customer', 'Customer'),
        ('Staff', 'Staff'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=Role_CHOICES, default='Customer')
    
    def __str__(self):
        return self.user.username
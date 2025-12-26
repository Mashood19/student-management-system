from django.db import models
from django.utils import timezone

class StudentSubmission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processed', 'Processed'),
        
    ]
    
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at'] 

# class UserNotificationStatus(models.Model):
#     user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
#     last_notifications_read = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"{self.user.username} - Last read: {self.last_notifications_read}"         
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    ROLE_CHOICES = [('Tenant', 'Tenant'),('Broker', 'Broker'),('Owner', 'Owner'),]
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
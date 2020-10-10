from django.db import models

class ContactUs(models.Model):
    Name = models.CharField(max_length = 100);
    Email = models.EmailField(max_length = 50);
    PhoneNumber = models.BigIntegerField(blank = True, null = True);
    Description = models.TextField();

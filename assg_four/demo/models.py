from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    time = models.DateTimeField()
    street_address = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day = models.CharField(max_length=10, choices=DAY_CHOICES)

    def __str__(self):
        return f"{self.time} - {self.street_address}"

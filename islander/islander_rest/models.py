from django.db import models

# Create your models here.

class FoodCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField(default='10')
    opens_at = models.CharField(max_length=100)
    closed_at = models.CharField(max_length=100)
    holiday_opens_at = models.CharField(max_length=100, default='')
    holiday_closed_at = models.CharField(max_length=100, default='')
    category = models.ForeignKey(FoodCategory, related_name='restaurants', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

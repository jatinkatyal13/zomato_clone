from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (
  MinValueValidator,
  MaxValueValidator
)

# Create your models here.
class Restaurant(models.Model):
  name = models.CharField(max_length = 256)
  address = models.TextField()
  veg_only = models.BooleanField(default = False)

  def __str__(self):
    return self.name

class Review(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  restaurant = models.ForeignKey('Restaurant', on_delete = models.CASCADE)
  title = models.CharField(max_length = 256)
  stars = models.IntegerField(validators = [MaxValueValidator(5), MinValueValidator(0)])
  body = models.TextField()

  def __str__(self):
    return self.title


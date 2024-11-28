from django.db import models

# Create your models here.
class Khoa(models.Model):
  ma_khoa = models.CharField(max_length=20)
  ten_khoa = models.CharField(max_length=128)

from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    age = models.IntegerField
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
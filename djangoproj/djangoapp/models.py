from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(null=True, blank=True)
    age = models.IntegerField(default=10)
    desc = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

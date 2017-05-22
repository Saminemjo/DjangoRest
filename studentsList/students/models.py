from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    def __str__(self):
        return self.first_name + " "+self.name

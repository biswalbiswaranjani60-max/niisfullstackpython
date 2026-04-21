from django.db import models

class Employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.FloatField()

    def __str__(self):
        return self.name
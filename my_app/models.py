from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=30)
    position = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.


class Supervisor(models.Model):
    supervisor_name = models.CharField(max_length=100)


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    company_description = models.TextField(blank=True, null=True)


class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_position = models.CharField(max_length=100)


class ArrivalTime(models.Model):
    employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employee_arrival = models.TimeField()



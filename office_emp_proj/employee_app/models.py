from django.db import models
import uuid


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    locatoin = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    emp_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    doj = models.DateField(auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

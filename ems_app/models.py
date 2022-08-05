from django.db import models


class Employee(models.Model):

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    dob = models.DateField()
    joining_date = models.DateField()
    jobs = models.ManyToManyField('Job', blank=True)

    def __str__(self) -> str:
        return self.first_name


class Job(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

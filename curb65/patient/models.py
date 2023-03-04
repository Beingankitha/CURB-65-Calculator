from django.db import models

# Create your models here.

class Patient(models.Model):
    patient_id = models.CharField(max_length=10, unique=True)
    dob = models.DateField()
    confusion = models.BooleanField()
    blood_urea = models.IntegerField()
    respiratory_rate = models.IntegerField()
    systolic_bp = models.IntegerField()
    diastolic_bp = models.IntegerField()
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.patient_id
    
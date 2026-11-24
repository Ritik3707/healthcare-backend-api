
from django.db import models
from django.conf import settings


class Doctor(models.Model):

    SPECIALIZATION_CHOICES = [
        ('Cardiologist', 'Cardiologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Neurologist', 'Neurologist'),
        ('Orthopedic', 'Orthopedic'),
        ('General Physician', 'General Physician'),
    ]

    name = models.CharField(max_length=100)

    specialization = models.CharField(
        max_length=100,
        choices=SPECIALIZATION_CHOICES
    )

    phone = models.CharField(max_length=15)

    email = models.EmailField(unique=True)

    experience = models.PositiveIntegerField()

    address = models.TextField()

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctors'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

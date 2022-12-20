from pyexpat import model
import uuid
import uuid
from django.db import models

# Create your models here.

class Employee(models.Model):
    """Model definition for Employee."""

    # TODO: Define fields here
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    image = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Employee."""

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        """Unicode representation of Employee."""
        pass


from django.db import models
from django.db.models.fields.related import ManyToManyField
from apps.department.models import Department

from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades(models.Model):
    """Model definition for Habilidades."""

    # TODO: Define fields here

    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        """Meta definition for Habilidades."""

        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        """Unicode representation of Habilidades."""
        return str(self.id) + ".- " + self.habilidad

class Person(models.Model):
    """Model definition for Person."""

    # TODO: Define fields here
    #Jobs
    jobs = [
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro')
    ]
    first_name = models.CharField('Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    job = models.CharField('Job', max_length=50, choices=jobs)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    # avatar = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        """Meta definition for Person."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Person."""
        return str(self.id) + '.- ' + self.first_name + '--' + self.last_name

    @property
    def complete_name(self):
        """Return de complete name"""
        return "%s %s" % (self.first_name, self.last_name)

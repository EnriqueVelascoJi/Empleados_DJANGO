from django.db import models

# Create your models here.
class Department(models.Model):
    """Model definition for Department."""

    # TODO: Define fields here
    name = models.CharField('Mame', max_length=50)
    short_name = models.CharField('Short name', max_length=50)
    anulate = models.BooleanField('Anulate', default=False)


    class Meta:
        """Meta definition for Department."""

        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        """Unicode representation of Department."""
        #El id lo a Django por defecto
        return str(self.id) + '.- ' + self.name + '--' + self.short_name

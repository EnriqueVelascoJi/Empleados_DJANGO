from django import forms

#Importamos el modelo 
from .models import Person

class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Person
        fields = ('__all__')

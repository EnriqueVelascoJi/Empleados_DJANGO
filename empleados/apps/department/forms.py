from django import forms

#Formulario de registro debido a una necesidad específica
    #Al agregar un nuevo departamento
    #es necesario que dicho departamento
    #contenga por defecto al menos un empleado
    #Por eso el registro se hace de esta manera
class NewDepartmentForm(forms.Form):
    """NewDepartmentForm definition."""

    # TODO: Define form fields here
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    department = forms.CharField(max_length=50)
    short_name = forms.CharField(max_length=20)



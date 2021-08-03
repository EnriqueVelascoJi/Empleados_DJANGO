from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#Vistas genericas
from django.views.generic.edit import FormView
from django.views.generic import ListView

#Importamos el formulario de registro
from .forms import NewDepartmentForm

#Importamos el modelo de persona y departamento
from apps.persona.models import Person
from .models import Department

# Create your views here.
#Nuevo departamento
class NewDepartmentView(FormView):
    
    template_name= 'Department/new_department.html'
    form_class = NewDepartmentForm
    success_url = '.'

    #Sobreescribimos la función
    def form_valid(self, form):
        # print('*******Estamos en el form valid')
        #Capturamos los datos del formulario
        name = form.cleaned_data['name']
        surname = form.cleaned_data['surname']
        department = form.cleaned_data['department']
        short_name_department = form.cleaned_data['short_name']

        #Registramos en el modelo departamento
        new_department = Department.objects.create(
            name = department,
            short_name = short_name_department
        )
        new_department.save()

        #Registramos en el modelo de empleado
        Person.objects.create(
           first_name = name,
           last_name = surname,
           job = '1',
           department = new_department
            
        )
        #La función create no necesita un .save()
        
        # print(name, surname, department, short_name_department)
        return super().form_valid(form)

#Listar departamento

class DepartmentListView(ListView):
    model = Department
    template_name = "Department/listDepartment.html"

    context_object_name = "departamentos"

    paginate_by = 10

    #Busqueda por nombre del departamento
    def get_queryset(self):

        name_departmet = self.request.GET.get('kword', '') 
        queryset = Department.objects.filter(
            name__contains = name_departmet
        )
        return queryset

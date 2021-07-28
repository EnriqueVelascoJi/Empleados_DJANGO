from django.db.models import query
from django.shortcuts import render

from django.views.generic import ListView, DetailView

#Import models
from .models import Habilidades, Person

# Create your views here.

#Lista todos los empleados
class ListAll(ListView):
    model = Person
    template_name = "Person/listPerson.html"

    #Paginación
    paginate_by = 5


#Lista los empleados por departamentos
class ListByDepartment(ListView):
    model = Person
    template_name = "Person/listByDepartment.html"

    #Filtrar por un departamento en específico

    # queryset = Person.objects.filter(
    #     department__name = "Economy"
    # )

    #Filtar por departamento
    def get_queryset(self):

        department = self.kwargs['name']
        print(department)
        queryset = Person.objects.filter(
            department__name = department
        )
        return queryset
    

#Lista de los empleados por Job
class ListByJob(ListView):
    model = Person
    template_name = "Person/listByJob.html"

    #Filtrar por trabajo --- kwargs toma el parámetro por URL
    def get_queryset(self):
        
        job_recover = self.kwargs['job']
        print(job_recover)
        queryset = Person.objects.filter(
            job = job_recover
        )
        return queryset

#Lista de los empleados por Palabra clave
class ListByKeyWord(ListView):
    model = Person
    template_name = "Person/listByKeyWord.html"

    context_object_name = 'empleados'

    def get_queryset(self):
        
        #Recuperamos el valor del formulario
        kword = self.request.GET['kword']
        queryset = Person.objects.filter(
            first_name__contains = kword
        )
        return queryset


#Listar Habilidades de un empleado (Many to Many)
class ListHabilidades(ListView):
    model = Person
    template_name = "Person/habilidades.html"

    context_object_name = 'habilidades'

    def get_queryset(self):

        #Recuperar el id del fomulario
        id_empleado = self.request.GET['id_empleado']

        #Recuperamos un empleado
        empleado = Person.objects.get(id = id_empleado)

        #Recuperamos las habilidades de ese regsitro
        habilidades = empleado.habilidades.all()    
        return habilidades


class PersonDetailView(DetailView):
    model = Person
    template_name = "Person/detailPerson.html"

    context_object_name = 'empleado'

    #slug -- Mejora en el posicionamiento (SEO)
    
    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empelado del Mes'
        return context
    

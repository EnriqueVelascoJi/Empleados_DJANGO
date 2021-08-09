from django.forms.forms import Form
from django.shortcuts import render, HttpResponse

from django.views.generic import (
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    TemplateView,
                                    UpdateView,
                                    DeleteView,
                                    FormView
                                )
from django.views.generic.edit import FormView

#Import models
from .models import Habilidades, Person

#Ayuda al redireccionamiento de url´s
from django.urls import reverse_lazy

# Create your views here.

#Pagina de inicio
class InicioView(TemplateView):
    """Vista que carga la pagina de inicio"""
    template_name = "inicio.html"



#Lista todos los empleados
class ListAll(ListView):
    model = Person
    template_name = "Person/listPerson.html"

    context_object_name = "empleados"

    #Paginación
    paginate_by = 10

    def get_queryset(self):
        
    #Recuperamos el valor del formulario
        kword = self.request.GET.get('kword', '')
        queryset = Person.objects.filter(
            first_name__contains = kword
        )
        return queryset
       


#Lista los empleados por departamentos
class ListByDepartment(ListView):
    model = Person
    template_name = "Person/listByDepartment.html"

    context_object_name = "empleados"
    paginate_by = 10

    #Filtrar por un departamento en específico

    # queryset = Person.objects.filter(
    #     department__name = "Economy"
    # )

    #Filtar por departamento
    def get_queryset(self):

        department = self.kwargs['name']
        # print(department)

        queryset = Person.objects.filter(
            department__name = department
        )
        return queryset
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department = self.kwargs['name']
        context['department'] = department
        return context


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
        kword = self.request.GET.get('kword', '')
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
        id_empleado = self.request.GET.get('id_empleado', '')

        #Recuperamos un empleado
        empleado = Person.objects.get(id = id_empleado)

        #Recuperamos las habilidades de ese regsitro
        habilidades = empleado.habilidades.all()    
        return habilidades

#Detalle de un empleado
class EmpleadoDetailView(DetailView):
    model = Person
    template_name = "Person/detailPerson.html"

    context_object_name = 'empleado'
    

    #slug -- Mejora en el posicionamiento (SEO)
    
    #Método de edicición del contexto
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empelado del Mes'
        print(context['object'].avatar)
        return context


class Success(TemplateView):
    template_name = "Person/success.html"

#Creación
class EmpleadoCreateView(CreateView):
    model = Person
    template_name = "Person/addEmpleado.html"

    #Campos que queremos registrar por defecto
    # fields = ['first_name','job']
    fields = ('__all__')

    #Vista de redireccionamiento una vez se haya agregado
    #Redireccionameinto a la mimsa URL
    # success_url = '.'
    success_url = reverse_lazy('person_app:list_all')

    #Validamos el formulario
    def form_valid(self, form):
        #Lógica del proceso
        empleado = form.save()
        return super().form_valid(form)
    
    #En caso de haber errores
    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))

#Update 

class EmpleadoUpdateView(UpdateView):
    model = Person
    template_name = "Person/update.html"

    fields = ('__all__')

   #Vista de redireccionamiento una vez se haya agregado
    #Redireccionameinto a la mimsa URL
    # success_url = '.'
    success_url = reverse_lazy('person_app:list_all')

    #Intersectamos los datos del formulario antes de que sean
    #validados y/o guardados para rutinas previas
    def post(self, request, *args: str, **kwargs):
        self.object = self.get_object()
        # print('==============')
        # print(request.POST)
        first_name = request.POST['first_name']
        # print(first_name)
        return super().post(request, *args, **kwargs)

    #Validamos el formulario
    def form_valid(self, form):
        #Lógica del proceso
        empleado = form.save()
        return super().form_valid(form)
    
    #En caso de haber errores
    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))

#Delete
class EmpleadoDeleteView(DeleteView):
    model = Person
    #El templete sirve como confirmación de la elimnación
    template_name = "Person/delete.html"

    success_url = reverse_lazy('person_app:list_all')

    #Intersección del formulario previo a su eliminación
    def delete(self, request, *args: str, **kwargs):
        return super().delete(request, *args, **kwargs)


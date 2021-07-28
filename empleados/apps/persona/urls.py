from django.urls import path

#Import Views
from . import views

app_name = 'person_app'

    
urlpatterns = [
    path('list_all/', views.ListAll.as_view(), name='list_all'),
    path('list_by_department/<name>/', views.ListByDepartment.as_view(), name='list_by_department'),
    path('list_by_job/<job>/', views.ListByJob.as_view(), name='list_by_job'),
    path('list_by_kword/', views.ListByKeyWord.as_view(), name='list_by_kword'),
    path('list_habilidades/', views.ListHabilidades.as_view(), name='list_habilidades'),
    path('ver_empleado/<pk>', views.PersonDetailView.as_view(), name='ver_empleado')
]

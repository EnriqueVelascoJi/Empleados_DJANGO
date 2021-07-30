from django.urls import path

# Import Views
from . import views

app_name='department_app'

urlpatterns = [
    path('new_department/', views.NewDepartmentView.as_view(), name="new_department"),

]
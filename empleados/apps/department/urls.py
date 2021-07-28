from django.urls import path

# Import Views
from . import views

app_name='department_app'

urlpatterns = [
    path('second_path/', views.second_view, name="second_path" )
]
from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patient_list, name='patients_list'),
]
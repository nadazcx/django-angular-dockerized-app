from django.urls import path
from . import views

urlpatterns = [
    path('add_employee/', views.add_employee, name='add_employee'),
    path('get_employee_all/', views.get_employee_all, name='get_employee_all'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_employees),
    path('add-employee',views.add_employees),
    path('add-dept',views.add_dept),
    path('delete-dept/<int:id>',views.delete_dept, name = "deletedept"),
    path('delete-employee/<int:id>',views.delete_employee, name = "deleteemployee"),
    
]
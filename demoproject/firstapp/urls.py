from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_employees),
    path('add-employee',views.add_employees,name= 'addemployee'),
    path('add-dept',views.add_dept, name='adddept'),
    path('delete-dept/<int:id>',views.delete_dept, name = "deletedept"),
    path('delete-employee/<int:id>',views.delete_employee, name = "deleteemployee"),
    path('edit-dept/<int:id>',views.edit_dept, name = "editedept"),
    path('edit-employee/<int:id>',views.edit_employee, name = "editemployee"),
    
]
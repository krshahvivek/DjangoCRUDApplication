from django.contrib import admin
from .models import Dept, Employess
# Register your models here.

@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
    list_display = ('id','code','name')

@admin.register(Employess)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','ecode','name','dept','dob','salary')
# admin.site.register(Dept)
# admin.site.register(Employess)


from django import forms
from .models import Dept, Employess

class DeptForm(forms.ModelForm):
    class Meta:
        model = Dept
        fields = ['code','name']
        widget = {
            'code': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }

class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employess
        fields = ['ecode','name','dob','dept','salary']
        widget = {
            'ecode': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control'}),
            'salary': forms.NumberInput(attrs={'class':'form-control'}),
        }
        dept= forms.ModelChoiceField(queryset=Dept.objects.all(), widget=forms.Select(attrs={'class':'form-control'})),

# class NewListingForm(forms.ModelForm):
#     # rest of your fields
#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(),

#     )
#     category.widget.attrs.update({'class': 'form-control'})

# class NewListingForm(forms.ModelForm):
#     # rest of your fields
#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-control'})
#         # `ModelChoiceField` is using the `Select` widget bu default

#     )
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'job_title', 'salary']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job title'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter salary'}),
        }

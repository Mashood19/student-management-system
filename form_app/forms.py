from django import forms
from .models import StudentSubmission

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentSubmission
        fields = ['name', 'contact', 'course']  
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your full name'
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Phone or email address'
            }),
            'course': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
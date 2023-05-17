from .models import *
from django import forms


class CreateStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'middle_name', 'last_name', 'email')

from django import forms
 
from .models import Dbms_Question
 
class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = Dbms_Question
        fields =[ 'number','description'
        ] 
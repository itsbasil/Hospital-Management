from django import forms
from.models import Patient,Doctor

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"
        widgets ={

        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"
        widgets ={

        }
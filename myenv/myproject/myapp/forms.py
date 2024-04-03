from django import forms
from.models import Patient,Doctor,Appointment

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

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields="__all__"
        widgets ={

        }
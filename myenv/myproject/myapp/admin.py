from django.contrib import admin
from.models import Patient,Appointment,Doctor,Contact
# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Contact)
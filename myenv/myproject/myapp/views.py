from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from.forms import PatientForm,DoctorForm,AppointmentForm
from.models import Patient,Doctor,Appointment
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

#patient Registration
def patientReg(request):
    if request.method == "POST":
        username=request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                return redirect('patientReg')
            user = User.objects.create_user(username=username, password=password)
            user.save()
        else:
            return redirect('patientReg')
        return redirect('/')
    else:
        return render(request,'patientReg.html')
    
    #doctor Registration
def doctorReg(request):
    if request.method == "POST":
        username=request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                return redirect('doctorReg')
            user = User.objects.create_user(username=username, password=password)
            user.save()
        else:
            return redirect('doctorReg')
        return redirect('/')
    else:
        return render(request,'doctorReg.html')

#patient Login
def patientLog(request):
    return render(request,'patientLog.html')

#patient appointment
def appointment(request):
    if request.method=="POST":
            form=AppointmentForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'index.html')
    else:
        form=AppointmentForm()
        return render(request,'appointment.html')
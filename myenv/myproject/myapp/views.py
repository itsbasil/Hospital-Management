from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from.forms import PatientForm
from.models import Patient
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

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

def patientLog(request):
    return render(request,'patientLog.html')
def appointment(request):
    return render(request,'appointment.html')
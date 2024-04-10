from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from.forms import PatientForm,AppointmentForm,DoctorForm,ContactForm
from.models import Patient,Appointment,Login,Doctor,Contact
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

#patient Registration
def patientReg(request):
    if request.method == "POST":
        username=request.POST['pname']
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
        username=request.POST['doctorname']
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

#doctor page
def doctor(request):
    return render(request,'doctor.html')

#contact page
def contact(request):
    return render(request,'contact.html')


#patient and doctor login
def patientLog(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=Patient.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'UserModule.html')
            return render(request, 'patientLog.html')
        except:
             pass
        try:
           user=Login.objects.get(username=username,password=password)
           if user is not None:
               print(user)
               return render(request, 'index.html')
           #return render(request,'Adminmodule.html')
        except:
            pass

        try:
            user=Doctor.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'DoctorModule.html')
            return render(request,'patientLog.html')
        except:
             pass
    else:
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
    
    #patient contact
def contact(request):
    if request.method=="POST":
            form=ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'index.html')
    else:
        form=ContactForm()
        return render(request,'contact.html')
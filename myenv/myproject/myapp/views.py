from django.shortcuts import render

# Create your views here.


def index(request):
    return render (request, 'index.html')
def patientReg(request):
    return render (request, 'patientReg.html')
def patientLog(request):
    return render (request, 'patientLog.html')
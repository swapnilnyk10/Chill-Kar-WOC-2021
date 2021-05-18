from django.shortcuts import render
from form.models import collect
from form.models import Data
from  django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')
def homepage(request): 
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        Email = request.POST['Email']
        phone = request.POST['phone']
        BloodSugar = request.POST['BloodSugar']
        BloodPressureSystolic = request.POST['BloodPressureSystolic']
        BloodPressureDiastolic = request.POST['BloodPressureDiastolic']
        Pulse = request.POST['Pulse']
        SpO2 = request.POST['SpO2']
        Fever = bool( request.POST.get('Fever',False))
        Cough = bool (request.POST.get('Cough',False))
        Headache = bool (request.POST.get('Headache',False))
        InaCrowdedPlace =bool (request.POST.get('InaCrowdedPlace',False))

        send_mail(
            fname + lname,#Subject
            "Blood Sugar = " + BloodSugar  + " "+"Blood Pressure Systolic = "+ BloodPressureSystolic  + " " +"Blood Pressure Systolic = "+ BloodPressureDiastolic + " " + "Pulse = " + Pulse  + " "+ "SpO2 = " +SpO2 ,#Message
            Email,#From Email
            ['swapnilnayak9@gmail.com'],#To Email
        )

        ins = collect(firstname=fname,lastname=lname,Email=Email,phone=phone,BloodSugar=BloodSugar,BloodPressureSystolic=BloodPressureSystolic,BloodPressureDiastolic=BloodPressureDiastolic,Pulse=Pulse,SpO2=SpO2,Fever=Fever,Cough=Cough,Headache=Headache,InaCrowdedPlace=InaCrowdedPlace)
        
        ins.save()
    return render(request,'homepage.html')

def display(request):
    # name = request.POST['name']
    name = request.POST.get('name')
    data1 = collect.objects.all()
    for ins in data1:
        if name == ins.firstname:
            return render(request,"display.html",{'ins':ins})
            break
    else :
        sentence = "No entry found"
        return render(request,"display.html",{'sentence':sentence})
    
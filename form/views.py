from django.shortcuts import render, redirect
from .models import collect, Room, Message
from django.http import HttpResponse, JsonResponse
# from form.models import Data
from  django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')
def homepage(request): 
    room = request.GET['username']
    username = request.GET['username']
    phone =request.GET['room_name']
    return render(request,'homepage.html',{'room':room ,'username':username, 'phone':phone})
    
def check(request):    
    username = request.POST['fname']
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

    if(SpO2<= '80'):
         send_mail(
            username,#Subject
            "Phone :"+ phone +" " + "Blood Sugar = " + BloodSugar  + " "+"Blood Pressure Systolic = "+ BloodPressureSystolic  + " " +"Blood Pressure Systolic = "+ BloodPressureDiastolic + " " + "Pulse = " + Pulse  + " "+ "SpO2 = " +SpO2 ,#Message
            Email,#From Email
            ['swapnilnayak9@gmail.com'],#To Email
        )
        
    ins = collect(username=username,Email=Email,phone=phone,BloodSugar=BloodSugar,BloodPressureSystolic=BloodPressureSystolic,BloodPressureDiastolic=BloodPressureDiastolic,Pulse=Pulse,SpO2=SpO2,Fever=Fever,Cough=Cough,Headache=Headache,InaCrowdedPlace=InaCrowdedPlace)
        
    ins.save()

        
    return redirect('display.html'+'/?username='+username)

def display(request):
    # name = request.POST['name']
    name = request.GET.get('username')
    
    data1 = collect.objects.all()
    
    return render(request,"display.html",{'datas':data1,'name':name})
  
            
    

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})   

def doctor(request):
    

    all_room=Room.objects.all()
    room_id={
        "rooms":all_room
    }
    return render(request, 'doctor.html',room_id)         
    
from django.shortcuts import render,HttpResponse
from form.models import collect
# Create your views here.
def hello(request):
    return HttpResponse("Hello")
def index(request):
    return render(request,'index.html')
def homepage(request):
    if request.method=="POST":
        
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        ins = collect(firstname=fname,lastname=lname,phone=phone)
        ins.save()
    return render(request,'homepage.html')
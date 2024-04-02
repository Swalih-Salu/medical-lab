from django.shortcuts import render
from .models import bkapmt,TeleRadio,bkapmtHaemolgy,bkapmtBiochem,bkapmtImmuno
# Create your views here.
def Home(req):
    bked=bkapmt.objects.all
    if req.method=='POST':
        name=req.POST.get('name')
        number=req.POST.get('number')
        city=req.POST.get('city')
        
        data=bkapmt(name=name,number=number,city=city)
        data.save()
    return render (req,'index.html',{'bked':bked})

def Teleradio(req):
    enquire=TeleRadio.objects.all
    if req.method=='POST':
        name=req.POST.get('name')
        email=req.POST.get('email')
        number=req.POST.get('number')
        designation=req.POST.get('designation')
        city=req.POST.get('city')
        
        data=TeleRadio(name=name,email=email,number=number,designation=designation,city=city)
        data.save()
        
    return render (req,"tele-radiology.html",{'enquire':enquire})

def Hcp(req):
    return render(req,"HCP.html")

def Doc(req):
    return render(req,'doctor-consultitions.html')

def Gallery(req):
    return render(req,'gallery.html')

def Pws(req):
    return render(req,'PWS.html')

def Contact(req):
    return render(req,'contactus.html')

def Haematology(req):
    bked=bkapmtHaemolgy.objects.all
    if req.method=='POST':
        name=req.POST.get('name')
        number=req.POST.get('number')
        city=req.POST.get('city')
        
        data=bkapmtHaemolgy(name=name,number=number,city=city)
        data.save()
    return render (req,'Haematology.html',{'bked':bked})

def Biochemistry(req):
    bked=bkapmtBiochem.objects.all
    if req.method=='POST':
        name=req.POST.get('name')
        number=req.POST.get('number')
        city=req.POST.get('city')
        
        data=bkapmtBiochem(name=name,number=number,city=city)
        data.save()
    return render(req,'Biochemistry.html',{'bked':bked})

def Immunology(req):
    bked=bkapmtImmuno.objects.all
    if req.method=='POST':
        name=req.POST.get('name')
        number=req.POST.get('number')
        city=req.POST.get('city')
        
        data=bkapmtImmuno(name=name,number=number,city=city)
        data.save()
    return render(req,'Immunology.html',{'bked':bked})
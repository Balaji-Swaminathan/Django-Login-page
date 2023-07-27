from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Datas


def home(request):
    
    return render(request,"Home2.html")


def product(request):
     Name=(request.POST["Name"])
     dob=(request.POST["DOB"])
     password=(request.POST["Password"])
     course=(request.POST["Course"])
     address=(request.POST["Address"])
     mail=(request.POST["Mail"])
     obj=Datas(Name=Name,DOB=dob,Password=password,Course=course,Address=address,Mail=mail)
     obj.save()
     return render(request,"res.html")
     
def login(request):
     return render(request,"Home2.html")

def update(request):
     data=Datas.objects.values_list('Name',flat=True)
     print(list(data))
     Name=(request.POST["Name"])
     dob=(request.POST["DOB"])
     password=(request.POST["Password"])
     course=(request.POST["Course"])
     address=(request.POST["Address"])
     mail=(request.POST["Mail"])
     obj=Datas(Name=Name,DOB=dob,Password=password,Course=course,Address=address,Mail=mail)
     obj.save()
     return render(request,"res.html")
     return render(request,"update.html",{'value':data})




from django.shortcuts import render
from .models import Familia

def familiares(request):    

    familiar1=Familia(id=1,nombre="Hugo",apellido="D'Imperio",edad=63,parentesco="Padre",fecha_nacimiento="27/04/1959")
    familiar2=Familia(id=2,nombre="Patricia",apellido="Appelhans",edad=61,parentesco="Madre",fecha_nacimiento="19/11/1960")
    familiar3=Familia(id=3,nombre="Rosario",apellido="D'Imperio",edad=35,parentesco="Hermana",fecha_nacimiento="06/12/1986")
    familiar4=Familia(id=4,nombre="Victoria",apellido="D'Imperio",edad=27,parentesco="Hermana",fecha_nacimiento="19/09/1995")

    return render(request,"template_familiares.html",{'familia':[familiar1,familiar2,familiar3,familiar4]})

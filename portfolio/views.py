from django.shortcuts import render
from clients.models import Proyecto 

def error_404(request,Exception):
    return render(request,"error_404.html",{})

def listar_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request,'home.html', {'proyectos':proyectos})
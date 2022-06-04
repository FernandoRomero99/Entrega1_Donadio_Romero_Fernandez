from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def inicio(self):
    plantilla = loader.get_template('AppBlog/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def cafe(request):
    return render(request, 'AppBlog/cafe.html')

def platos(request):
    return render(request, 'AppBlog/platos.html')

def postres(request):
    return render(request, 'AppBlog/postres.html')

def quesos(request):
    return render(request, 'AppBlog/quesos.html')

def vinos(request):
    return render(request, 'AppBlog/vinos.html')





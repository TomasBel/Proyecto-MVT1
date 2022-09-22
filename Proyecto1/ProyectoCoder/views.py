from calendar import c
from re import template
from ast import MatchMapping
from unicodedata import name
from django.http import HttpResponse
from django.template import Template,  Context
from ProyectoCoder.models import MiFamily
from django.shortcuts import render


def probandoTemplate(self):

	miHtml = open("C:/Users/tomas/Desktop/Python/Proyecto1/Proyecto1/Plantillas/template1.html")

	plantilla = Template(miHtml.read())

	miHtml.close()

	miContexto = Context()

	documento = plantilla.render(miContexto)

	return HttpResponse(documento)

def Family(request):

	mama = MiFamily(nombre = "Carina", edad = 47, fecha_nac="1975-05-16")
	mama.save()
	papa = MiFamily(nombre = "Edgar", edad = 52, fecha_nac="1970-01-26")
	papa.save()
	hermano = MiFamily(nombre = "Ignacio", edad = 10, fecha_nac="2011-11-07" )
	hermano.save()
	
	#miHtml = open("C:/Users/tomas/Desktop/Python/Proyecto1/ProyectoCoder/templates/ProyectoCoder/Family.html")
	
	#plantilla = Template(miHtml.read())
	
	#miHtml.close()

	#miContexto = Context()

	#documento = plantilla.render(miContexto)
	
	return render(request, "ProyectoCoder/Family.html",{"mama":mama,"papa":papa,"hermano":hermano})
	

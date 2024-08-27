from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello Django !</h1>')

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch ! </p>')

def contact(request):
    return HttpResponse('<h1>Nos contacts : nom@mail.fr</h1>')

def help(request):
    return HttpResponse('<p>Besoin de nous ?</p>')

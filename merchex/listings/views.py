from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', 
                  {'bands': bands})

def linsting(request):
    return render(request, 'listings/listing.html')

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')

def help(request):
    return HttpResponse('<p>Besoin de nous ?</p>')

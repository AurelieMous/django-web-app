from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', 
                  {'bands': bands})

def band_detail(request, id):
  band = Band.objects.get(id=id) 
  return render(request,
          'listings/band_detail.html',
          {'band': band})

def listing(request): #page listing avec les objets
    listing = Listing.objects.all()
    return render(request, 'listings/listing.html',
                  {'listing': listing})

def listing_detail(request, id):
    listing_detail = Listing.objects.get(id=id)
    return render(request,
                  'listings/listing_detail.html',
                  {'listing_detail' : listing_detail})


def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')

def help(request):
    return HttpResponse('<p>Besoin de nous ?</p>')




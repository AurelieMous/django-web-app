from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm
from django.core.mail import send_mail
from django.shortcuts import redirect

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

def contact(request):
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    form = ContactUsForm()  # ajout d’un nouveau formulaire ici
    return render(request,
          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit
    

def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
        return redirect('email-sent')
    else:
        form = ContactUsForm()

    return render(request,
            'listings/contact.html',
            {'form': form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})
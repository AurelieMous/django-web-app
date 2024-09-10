from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
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

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()

    return render(request, 
                  'listings/listing_create.html', 
                  {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                'listings/band_update.html',
                {'form': form})

def listing_update(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request,
                'listings/listing_update.html',
                {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band_list')
    return render(request,
           'listings/band_delete.html',
           {'band': band})

def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        listing.delete()
        return redirect('listing')
    return render(request,
           'listings/listing_delete.html',
           {'listing': listing})
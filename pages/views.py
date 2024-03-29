from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, state_choices, bedroom_choices

# Create your views here.

def index(request):

    listings = Listing.objects.order_by('-list_data').filter(is_publish=True)[:3]

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,

    }

    return render(request, 'pages/index.html', context)

def about(request):

    realtors = Realtor.objects.all()
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request, 'pages/about.html', context)

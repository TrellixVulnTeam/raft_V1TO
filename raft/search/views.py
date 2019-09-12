from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

import random

from .raftYelp import find_rafts
from .models import ViewedRafts

from .forms import SearchForm

def home(request):
    #ViewedRafts.objects.create(name=name, rating=rating, num_reviews=num_reviews, price=price,
                               #address=address, city=city, state=state, zip_code=zip_code)

    #rafts = ViewedRafts.objects.all()
    
    form = SearchForm(request.GET, auto_id="%s-form")
    return render(request, 'home.html', {'form': form})

def search(request):
    form = SearchForm(request.POST, auto_id="mini-%s-form")

    if form.is_valid():
        term = form.cleaned_data['term']
        location = form.cleaned_data['location']
    else:
        term = ''
        location = 'Seattle'

    potential_RAFTs = find_rafts(location, term)

    num_RAFTs = len(potential_RAFTs)
    random_index = random.randint(0, num_RAFTs - 1)

    potential_RAFT = potential_RAFTs[random_index]
    name = potential_RAFT.name
    address = potential_RAFT.address
    price = potential_RAFT.price
    rating = potential_RAFT.rating
    image_url = potential_RAFT.image_url

    args = {
        'form': form,
        'name': name,
        'address': address,
        'price': price,
        'rating': rating,
        'image_url': image_url,
        }

    return render(request, 'search.html', args)


def about(request):
    return render(request, 'about.html')
    
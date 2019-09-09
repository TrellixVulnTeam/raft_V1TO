from django.shortcuts import render
from django.http import HttpResponse
import random

from .raftYelp import check_restaurants
from .models import ViewedRafts

from .forms import SearchForm

# Create your views here.
def home(request):
    #location = 'san diego'
    #cuisine = 'burgers'

    #potential_RAFTs = check_restaurants(location, cuisine)
    #num_RAFTs = len(potential_RAFTs)
    #rand_indexes = random.sample(range(num_RAFTs), num_RAFTs)

    #potential_RAFT = potential_RAFTs[0]

    #name = potential_RAFT.name
    #rating = potential_RAFT.rating
    #num_reviews = potential_RAFT.num_reviews
    #price = len(potential_RAFT.price)

    #address = potential_RAFT.address
    #city = potential_RAFT.city
    #state = potential_RAFT.state
    #zip_code = potential_RAFT.zip_code

    #ViewedRafts.objects.create(name=name, rating=rating, num_reviews=num_reviews, price=price,
                               #address=address, city=city, state=state, zip_code=zip_code)

    #rafts = ViewedRafts.objects.all()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            term = form.cleaned_data['term']
            location = form.cleaned_data['location']

            potential_RAFTs = check_restaurants(location, term)

            num_RAFTs = len(potential_RAFTs)
            random_index = random.randint(0, num_RAFTs - 1)

            potential_RAFT = potential_RAFTs[random_index]
            name = potential_RAFT.name
            address = potential_RAFT.address

            args = {
                'form': form,
                'name': name,
                'address': address
                }

        return render(request, 'home.html', args)
    else:
        form = SearchForm(request.GET)
        return render(request, 'home.html', {'form': form})
    
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

import random
import json

from .raftYelp import find_rafts, generate_indexes, create_args
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
    else: # If '/search' is manually entered in the url.
        term = ''
        location = 'Seattle'

    raft_list = find_rafts(location, term)
    
    if not raft_list: # Executes if no restaurants are found.
        return render(request, 'search.html', { 'form': form, 'name': 'NO RESTUARANTS FOUND.'})
        
    random_indexes = generate_indexes(raft_list)
    raft = raft_list[random_indexes[0]]

    args = create_args(raft)
    args['form'] = form

    return render(request, 'search.html', args)

def about(request):
    raft_list = find_rafts('seattle', 'chinese')
    json_string = json.dumps(raft_list[0].__dict__, indent=4)

    args = {
        'string': json_string
    }
    
    return render(request, 'about.html', args)

def contact(request):
    return render(request, 'contact.html')
    
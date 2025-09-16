from django.shortcuts import render, redirect
from .forms import PlaceForm
from datetime import datetime

def index(request):
    context = {
        'site_name': 'My Favorite Places',
        'site_description': 'Which I love, and not so much'
    }
    return render(request, 'places/index.html', context)

def places_list(request):
    if 'places' not in request.session:
        request.session['places'] = []
    
    places = request.session['places']
    context = {
        'places': places
    }
    return render(request, 'places/places_list.html', context)

def place_detail(request, place_id):
    places = request.session.get('places', [])
    place = None
    
    for p in places:
        if p['id'] == place_id:
            place = p
            break
    
    if not place:
        return redirect('places:places_list')
    
    context = {
        'place': place
    }
    return render(request, 'places/place_detail.html', context)

def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            if 'places' not in request.session:
                request.session['places'] = []
            
            places = request.session['places']
            new_place = {
                'id': len(places) + 1,
                'name': form.cleaned_data['name'],
                'description': form.cleaned_data['description'],
                'type': form.cleaned_data['type'],
                'location': form.cleaned_data['location'],
                'rating': form.cleaned_data['rating'],
                'created_date': datetime.now().strftime('%Y-%m-%d')
            }
            
            places.append(new_place)
            request.session['places'] = places
            request.session.modified = True
            
            return redirect('places:places_list')
    else:
        form = PlaceForm()
    
    return render(request, 'places/add_place.html', {'form': form})
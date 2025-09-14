from django.shortcuts import render

def index(request):
    context = {
        'site_name': 'My Favorite Places',
        'site_description': 'Places I love, and not so much'
    }
    return render(request, 'places/index.html', context)
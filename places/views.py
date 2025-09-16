from django.shortcuts import render, redirect
from .forms import PlaceForm
from datetime import datetime
from .random_place import random_place
from .data import get_default_places


def index(request):
    context = {
        "site_name": "My Favorite Places",
        "site_description": "Which I love, and not so much",
    }

    if request.method == "POST" and "random_place" in request.POST:
        user_places = request.session.get("places", [])
        default_places = get_default_places()
        all_places = default_places + user_places

        selected_place = random_place(all_places)
        if selected_place:
            context["random_place"] = selected_place

    return render(request, "places/index.html", context)


def places_list(request):
    if "places" not in request.session:
        request.session["places"] = []

    user_places = request.session["places"]
    default_places = get_default_places()
    all_places = default_places + user_places

    context = {"places": all_places}
    return render(request, "places/places_list.html", context)


def place_detail(request, place_id):
    user_places = request.session.get("places", [])
    default_places = get_default_places()
    all_places = default_places + user_places

    place = None
    for p in all_places:
        if p["id"] == place_id:
            place = p
            break

    if not place:
        return redirect("places:places_list")

    context = {"place": place}
    return render(request, "places/place_detail.html", context)


def add_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            if "places" not in request.session:
                request.session["places"] = []

            places = request.session["places"]
            default_places = get_default_places()
            all_places = default_places + places

            if all_places:
                new_id = max(p["id"] for p in all_places) + 1
            else:
                new_id = 1

            new_place = {
                "id": new_id,
                "name": form.cleaned_data["name"],
                "description": form.cleaned_data["description"],
                "type": form.cleaned_data["type"],
                "location": form.cleaned_data["location"],
                "rating": form.cleaned_data["rating"],
                "created_date": datetime.now().strftime("%Y-%m-%d"),
            }

            places.append(new_place)
            request.session["places"] = places
            request.session.modified = True

            return redirect("places:places_list")
    else:
        form = PlaceForm()

    return render(request, "places/add_place.html", {"form": form})

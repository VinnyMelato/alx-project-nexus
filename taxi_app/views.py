from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Taxi, TaxiRank
from .forms import ReviewForm
import math

def search(request):
    destination = request.GET.get('destination', '').strip()
    user_lat = request.GET.get('latitude')
    user_lon = request.GET.get('longitude')
    results = []

    if destination:
        taxis = Taxi.objects.filter(destination__icontains=destination, available=True)
    else:
        taxis = Taxi.objects.filter(available=True)

    if taxis:
        if user_lat and user_lon:
            try:
                user_lat = float(user_lat)
                user_lon = float(user_lon)
                for taxi in taxis:
                    rank = taxi.rank
                    dlat = math.radians(rank.latitude - user_lat)
                    dlon = math.radians(rank.longitude - user_lon)
                    a = math.sin(dlat/2)**2 + math.cos(math.radians(user_lat)) * math.cos(math.radians(rank.latitude)) * math.sin(dlon/2)**2
                    c = 2 * math.asin(math.sqrt(a))
                    distance = 6371 * c
                    rank.distance = distance
                    taxi.rank = rank
                    results.append(taxi)
                results.sort(key=lambda x: x.rank.distance)
                results = results[:1]
            except (ValueError, TypeError):
                results = list(taxis)
        else:
            results = list(taxis)
    return render(request, 'taxi_app/search.html', {'results': results})

def route(request, rank_id):
    rank = TaxiRank.objects.get(id=rank_id)
    return render(request, 'taxi_app/route.html', {'rank': rank})

@login_required
def add_review(request, taxi_id):
    taxi = Taxi.objects.get(id=taxi_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.taxi = taxi
            review.user = request.user  # Sets the logged-in user
            review.save()
            return HttpResponseRedirect('/search/')
    else:
        form = ReviewForm()
    return render(request, 'taxi_app/add_review.html', {'form': form, 'taxi': taxi})
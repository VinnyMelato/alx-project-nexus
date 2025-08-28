from django.urls import path
from .views import search, route, add_review

urlpatterns = [
    path('', search, name='home'),  # Add this for the root URL
    path('search/', search, name='search'),
    path('route/<int:rank_id>/', route, name='route'),
    path('review/<int:taxi_id>/', add_review, name='add_review'),
]
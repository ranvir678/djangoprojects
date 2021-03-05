from django.shortcuts import render
from .models import Flight
from django.urls import reverse
from 
# Create your views here.
def index(request):
    flights=Flight.objects.all
    return render(request,"flight/index.html",
    {"flights":flights}
    )
def flight(request,flight_id):
    flight=Flight.objects.get(id=flight_id)
    #Here in the argument in place of id we can also give 'pk' which refers to primary key
    return render(request,"flight/flight.html",{
    "flight":flight,
    "passengers":flight.passengers.all()
    })
def book(request,flight_id):
    if request.method=="POST":
        flight=Flight.objects.get(id=flight_id)
        passenger=Passenger.objects.get(pk=int(request.POST['passenger']))
        passenger.flights.add(flight)

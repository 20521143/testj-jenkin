from django.shortcuts import render, HttpResponseRedirect
from .models import Flight, Airport, Passenger
from django.urls import reverse
from . forms import FlightForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
    
def flight(request, flight_id):
    flight=Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })
    
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        
        passenger_id = int(request.POST['passenger'])
        
        passenger = Passenger.objects.get(pk=passenger_id)
        
        passenger.flights.add(flight)
        
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

# Add new Flight
def add(request):
    
    if request.method == 'POST':
        form = FlightForm(request.POST)
        
        if form.is_valid() :#and float(request.POST['duration']) > 0:
            form.save()
            
            messages.success(request, "Flight added successfully")
            return HttpResponseRedirect(reverse("flights:index"))
        else:
            messages.error(request, "The information of flight is invalid")
            return HttpResponseRedirect(reverse("flights:add_flight"))
    else:
        form = FlightForm()
        
        
    return render(request, "flights/add-flight.html", {
        'form': form,
    })
    

    

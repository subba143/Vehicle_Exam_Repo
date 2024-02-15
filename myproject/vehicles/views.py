from django.shortcuts import render
from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import VehicleForm
# Create your views here.
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_data/list.html', {'vehicles': vehicles})


def vehicle_details(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'vehicle_data/vehicle_details.html', {'vehicle': vehicle})

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicle_data/add_vehicle.html', {'form': form})

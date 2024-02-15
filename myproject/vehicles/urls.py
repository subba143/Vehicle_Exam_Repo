from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet
from vehicles import views
router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('v_list/', views.vehicle_list),
    path('v_details/<int:vehicle_id>/', views.vehicle_details, name='vehicle_details'),
    path('v_add/', views.add_vehicle),

]

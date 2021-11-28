from django.urls import path
from django.urls import include
from parqueadero.views.parkingView import ParkingCreateView, ParkingListView,ParkingDetailView, ParkingUpdateView, ParkingDeleteView



urlpatterns = [
 
      
    path("parking/create/", ParkingCreateView.as_view()),
    path("parking/list/", ParkingListView.as_view()),
    path("parking/<int:pk>/", ParkingDetailView.as_view()),
    path("parking/update/<int:pk>/", ParkingUpdateView.as_view()),
    path("parking/delete/<int:pk>/", ParkingDeleteView.as_view()),
   
]

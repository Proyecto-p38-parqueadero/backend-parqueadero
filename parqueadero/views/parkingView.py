from rest_framework                          import generics
from parqueadero.models.parking_lot               import Parking
from parqueadero.serializers.parkingSerializer import ParkingSerializer


class ParkingCreateView(generics.CreateAPIView):
    queryset         = Parking.objects.all()
    serializer_class = ParkingSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ParkingListView(generics.ListAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ParkingDetailView(generics.RetrieveAPIView):
    queryset         = Parking.objects.all()
    serializer_class = ParkingSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class ParkingUpdateView(generics.UpdateAPIView):
    queryset         = Parking.objects.all()
    serializer_class = ParkingSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class ParkingDeleteView(generics.DestroyAPIView):
    queryset         = Parking.objects.all()
    serializer_class = ParkingSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
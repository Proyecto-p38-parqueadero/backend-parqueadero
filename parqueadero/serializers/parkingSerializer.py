from rest_framework import serializers
from parqueadero.models.parking_lot   import Parking


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = [ "nombre", "administrador", "telefono", "direccion", "email", "ciudad"]

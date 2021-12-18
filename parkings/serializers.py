from rest_framework import serializers
from .models import Parking


class ParkingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parking
        fields = ('id',
                  'address',
                  'rate',
                  'count_places',
                  'parking_price')

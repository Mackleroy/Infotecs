from rest_framework import serializers

from Shops.models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'name']


class StreetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Street
        fields = ['id', 'name']


class ShopListSerializer(serializers.ModelSerializer):
    street = serializers.CharField(source='street.name')
    city = serializers.CharField(source='street.city.name')

    class Meta:
        model = Shop
        fields = ['id', 'name', 'city', 'street',
                  'house', 'open_time', 'close_time']


class ShopCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ['name', 'street', 'house', 'open_time', 'close_time']

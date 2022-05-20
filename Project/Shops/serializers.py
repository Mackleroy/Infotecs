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


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ['name', 'city', 'street', 'house', 'open_time', 'close_time']

from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from Shops.filters import ShopCustomFilter
from Shops.models import City, Shop
from Shops.serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer

    @action(methods=['GET'], detail=True)
    def street(self, request, pk):
        """Returns list of city's streets"""
        city = self.get_object()  # throw 404 if city now found
        serialized_streets = StreetSerializer(city.streets.all(), many=True)
        # we can't filter streets by 'city=pk', cuz pk may be unreal
        return Response(data=serialized_streets.data, status=status.HTTP_200_OK)


class ShopViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [ShopCustomFilter]

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        shop_instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'shop_id': shop_instance.id},
                        status=status.HTTP_201_CREATED, headers=headers)

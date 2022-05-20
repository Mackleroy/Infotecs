from django.urls import path, include

from Shops.views import CityViewSet, ShopViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register('city', CityViewSet)
router.register('shop', ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

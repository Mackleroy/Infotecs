import datetime

from django.db.models import Q
from django.utils import timezone
from rest_framework import filters


class ShopCustomFilter(filters.BaseFilterBackend):
    """
    Filter for street, city fields and open status in Shop model.
    """
    def filter_queryset(self, request, queryset, view):
        query_params = request.query_params
        open_state = query_params.get('open')
        current_time = timezone.now().time()
        q = Q()

        if query_params.get('street'):
            q &= Q(street=query_params.get('street'))
        if query_params.get('city'):
            q &= Q(city=query_params.get('city'))

        if open_state == '1':
            q &= Q(open_time__lt=current_time, close_time__gt=current_time)
        elif open_state == '0':
            q &= Q(
                Q(open_time__gt=current_time) | Q(close_time__lt=current_time)
            )

        return queryset.filter(q)

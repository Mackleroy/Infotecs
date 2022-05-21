from datetime import datetime

from django.db.models import Q, F
from rest_framework import filters


#  it also may be in settings.py
OPENED_QUERY_PARAM_VALUE = '1'
CLOSED_QUERY_PARAM_VALUE = '0'


class ShopCustomFilter(filters.BaseFilterBackend):
    """
    Filter for street, city fields and open status in Shop model.
    """
    def filter_queryset(self, request, queryset, view):
        query_params = request.query_params
        open_state = query_params.get('open')
        current_time = datetime.now().time()
        q = Q()

        if query_params.get('street'):
            q &= Q(street=query_params.get('street'))
        if query_params.get('city'):
            q &= Q(city=query_params.get('city'))

        if open_state == OPENED_QUERY_PARAM_VALUE:
            q &= Q((
                # day shop case, open and close time during one day
                Q(
                    Q(open_time__lt=F('close_time')) &
                    Q(open_time__lt=current_time, close_time__gt=current_time)
                ) |
                # night shop case, open time in the evening,
                # close time in the morning of the next day
                Q(
                    Q(open_time__gt=F('close_time')) & Q(
                        Q(open_time__lt=current_time) |
                        Q(close_time__gt=current_time))
                )
            ))
        elif open_state == CLOSED_QUERY_PARAM_VALUE:
            q &= Q((
                # day shop case, open and close time during one day
                Q(
                    Q(open_time__lt=F('close_time')) & Q(
                        Q(open_time__gt=current_time) |
                        Q(close_time__lt=current_time))
                ) |
                # night shop case, open time in the evening,
                # close time in the morning of the next day
                Q(
                    Q(open_time__gt=F('close_time')) &
                    Q(open_time__gt=current_time, close_time__lt=current_time)
                )
            ))

        return queryset.filter(q)

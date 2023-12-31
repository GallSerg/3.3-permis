from django_filters import rest_framework as filters

from .models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    creator = filters.NumberFilter(field_name='creator')
    created_at = filters.DateFromToRangeFilter(field_name='created_at')
    status = filters.CharFilter(field_name='status')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
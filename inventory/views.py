from rest_framework import viewsets, filters
from .models import InventoryItem
from .serializers import InventoryItemSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'quantity', 'price']

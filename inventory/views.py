from .models import Item
from .serializers import ItemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

# View for listing all items and creating a new item
class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['quantity', 'price']  # Add fields you want to filter by
    search_fields = ['name', 'description']


# View for retrieving, updating, and deleting an item
class ItemDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()  # Fetch all items
    serializer_class = ItemSerializer  # Serialize data

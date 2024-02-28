from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Item
from .serializers import ItemSerializer
from .filters import ItemFilter
from django.db.models import Q


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ItemFilter
    ordering_fields = ['name', 'category', 'quantity', 'price']  # Fields you allow to be sorted

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(category__icontains=search_query)  # Assuming you want to search by category too
            )
        return queryset



class ItemDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all() 
    serializer_class = ItemSerializer  

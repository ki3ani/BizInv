from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .models import Item
from .serializers import ItemSerializer
from .filters import ItemFilter
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Item


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'item_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', None)
        category_query = self.request.GET.get('category', None)
        min_price = self.request.GET.get('min_price', None)
        max_price = self.request.GET.get('max_price', None)

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(category__icontains=search_query)
            )

        if category_query:
            queryset = queryset.filter(category__icontains=category_query)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset
    

    
class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'item_detail.html'


# Define the custom pagination class
class SmallResultSetPagination(PageNumberPagination):
    page_size = 10  # Adjust the number of items per page as needed
    page_size_query_param = 'page_size'  # Allows client to override the page size via query parameter
    max_page_size = 100  # Maximum limit allowed for page_size

# The view for listing and creating items, now with pagination
class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ItemFilter
    ordering_fields = ['name', 'category', 'quantity', 'price']  # Fields you allow to be sorted
    pagination_class = SmallResultSetPagination  # Use the custom pagination class

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

# The view for retrieving, updating, and deleting items
class ItemDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

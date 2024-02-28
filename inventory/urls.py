# urls.py

from django.urls import path
from .views import ItemCreateView, ItemUpdateView, ItemDeleteView, ItemListView, ItemDetailView, home

urlpatterns = [
    path('', home, name='home'),
    path('items/', ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('items/create/', ItemCreateView.as_view(), name='item_create'),
    path('items/<int:pk>/update/', ItemUpdateView.as_view(), name='item_update'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]

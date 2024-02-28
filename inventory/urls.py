# urls.py

from django.urls import path
from .views import InventoryQuantityByCategoryView, InventoryValueByCategoryView, ItemCreateView, ItemUpdateView, ItemDeleteView, ItemListView, ItemDetailView, LowStockItemsView, MostValuableItemsView, ReportsView, home

urlpatterns = [
    path('', home, name='home'),
    path('items/', ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('items/create/', ItemCreateView.as_view(), name='item_create'),
    path('items/<int:pk>/update/', ItemUpdateView.as_view(), name='item_update'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
    path('reports/', ReportsView.as_view(), name='reports_page'),
    path('reports/inventory_value_by_category/', InventoryValueByCategoryView.as_view(), name='inventory_value_by_category'),
    path('reports/low_stock_items/', LowStockItemsView.as_view(), name='low_stock_items'),
    path('reports/most_valuable_items/', MostValuableItemsView.as_view(), name='most_valuable_items'),
    path('reports/inventory_quantity_by_category/', InventoryQuantityByCategoryView.as_view(), name='inventory_quantity_by_category')
]

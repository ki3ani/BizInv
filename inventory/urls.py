from django.urls import path
from .views import ItemListCreate, ItemDetailUpdateDelete

urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetailUpdateDelete.as_view(), name='item-detail-update-delete'),
]

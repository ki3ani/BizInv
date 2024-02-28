from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import ItemForm
from django.db.models import Q





def home(request):
    return render(request, 'home.html')

class ItemCreateView(CreateView):
    model = Item
    template_name = 'inventory/item_create.html'
    form_class = ItemForm
    success_url = reverse_lazy('item_list')

class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'inventory/item_update.html'
    form_class = ItemForm

    def get_success_url(self):
        return reverse_lazy('item_detail', kwargs={'pk': self.object.pk})

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'inventory/item_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('item_list')

class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'inventory/item_list.html'
    paginate_by = 10 

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
    template_name = 'inventory/item_detail.html'

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import ItemForm
from django.db.models import Q
from django.views.generic import TemplateView
from django.db.models import Sum, F




def home(request):
    return render(request, 'inventory/home.html')

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_choices'] = Item.CATEGORY_CHOICES
        return context

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


class InventoryValueByCategoryView(TemplateView):
    template_name = 'inventory/inventory_value_by_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate total value of items in each category
        category_values = Item.objects.values('category')\
            .annotate(total_value=Sum(F('price')*F('quantity')))\
            .order_by('category')

        context['category_values'] = category_values
        return context
    


class LowStockItemsView(ListView):
    template_name = 'inventory/low_stock_items.html'
    context_object_name = 'low_stock_items'

    def get_queryset(self):
        # Items with quantity less than a threshold (e.g., 5)
        return Item.objects.filter(quantity__lt=5)
    

class MostValuableItemsView(ListView):
    template_name = 'inventory/most_valuable_items.html'
    context_object_name = 'most_valuable_items'

    def get_queryset(self):
        return Item.objects.annotate(total_value=F('price') * F('quantity')).order_by('-total_value')[:10]  # Top 10



class CategorySummaryReportView(TemplateView):
    template_name = 'inventory/category_summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_summary = Item.objects.values('category')\
            .annotate(total_quantity=Sum('quantity'), total_value=Sum(F('quantity') * F('price')))\
            .order_by('category')

        context['category_summary'] = category_summary
        return context


class ReportsView(TemplateView):
    template_name = 'inventory/reports_page.html'



class InventoryQuantityByCategoryView(TemplateView):
    template_name = 'inventory/inventory_quantity_by_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Item.objects.values('category').annotate(total_quantity=Sum('quantity'))
        context['categories'] = categories
        return context

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Product, Supermarket
from django.db.models import F

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'groceries_manager/index.html'
    context_object_name = 'index_view'

    def get_queryset(self):
        """
        
        """
        return Product.objects.all()[:5]

class DetailView(generic.DetailView):
    model = Product
    template_name = 'groceries_manager/detail.html'

class ResultsView(generic.DetailView):
    model = Supermarket
    template_name = 'groceries_manager/results.html'

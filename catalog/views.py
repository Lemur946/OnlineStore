from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy

from .models import Product
from django.views.generic import UpdateView, CreateView, ListView, DetailView, TemplateView
from .forms import ProductForm


# Creating a CBV for the homepage
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'  # Specify the path to the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Skystore - Главная'
        return context


# Create a CBV for the contact page
class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'  # Specify the path to the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Skystore - Контакты'
        return context


# Creating a CBV for a product detail page
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['title'] = f'Skystore - {product.name}'
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, Http404
from django.urls import reverse_lazy, reverse

from .models import Product
from django.views.generic import UpdateView, CreateView, ListView, DetailView, TemplateView, DeleteView
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['title'] = f'Skystore - {product.name}'
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price',)  # Removed 'owner' from fields
    success_url = reverse_lazy('catalog:home')
    login_url = reverse_lazy('users:login')  # Where to redirect if the user is not logged in

    def form_valid(self, form):
        # We receive the object but do not save it to the database.
        self.object = form.save(commit=False)
        # Assign the current user as the owner
        self.object.owner = self.request.user
        # Now we save the object to the database
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'image',)  # The owner does not change
    success_url = reverse_lazy('catalog:home')
    login_url = reverse_lazy('users:login')

    def test_func(self):
        """
        Verifying that the user is the owner of the product.
        """
        product = self.get_object()
        return self.request.user == product.owner

    def handle_no_permission(self):
        """
        If the user does not have rights, we return error 404 (or 403).
        """
        raise Http404("У вас нет прав для редактирования этого продукта")


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    login_url = reverse_lazy('users:login')

    def test_func(self):
        """
        Verifies that the user is the product owner
        OR is a member of the 'Product Moderator' group
        """
        product = self.get_object()
        user = self.request.user

        # Owner verification
        is_owner = (user == product.owner)

        # Checking for moderator rights (including the right to delete)
        can_delete = user.has_perm('catalog.delete_product')

        # Access is allowed if at least one of the conditions is met
        return is_owner or can_delete

    def handle_no_permission(self):
        raise Http404("У вас нет прав для удаления этого продукта")

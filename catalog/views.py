from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Product


def home(request: HttpRequest) -> HttpResponse:
    """
    Controller for displaying the home page.

Receives a request object and returns a rendered HTML template
of the home page.
    """
    # Just render and return the main page template
    return render(request, 'catalog/home.html')


def contacts(request: HttpRequest) -> HttpResponse:
    """
    Controller for displaying the contact page and processing the form.
    """
    # Check if the request was sent using the POST method
    if request.method == 'POST':
        # If yes, then we extract the data from the request.POST object
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Output the received data to the console for debugging.
        # In the future, this could include logic for sending emails or saving to a database.
        print(f'Новое сообщение от {name} (Телефон: {phone}): {message}')

    # Regardless of the method, we render and return the contact page template
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk: int):
    """
    A controller for displaying detailed product information.
    """
    # Get the product object or return 404 if it is not found
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product,
        'title': f'Продукт - {product.name}'  # Dynamic Page Title
    }
    return render(request, 'catalog/product_detail.html', context)

# catalog/urls.py
from django.urls import path
from .views import home, contacts

# Это нужно для того, чтобы Django мог однозначно определять
# URL-имена, принадлежащие этому приложению.
app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
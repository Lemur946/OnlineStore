from django.urls import path
from django.views.generic import DeleteView

from .views import (BlogCreateView, BlogListView, BlogDetailView,
                    BlogUpdateView)

app_name = 'blog'

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
]

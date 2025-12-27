from django.urls import path
from .views import (BlogCreateView, BlogListView, BlogDetailView,
                    BlogUpdateView, BlogDeleteView)
from typing import List, Union
from django.urls.resolvers import URLResolver, URLPattern

app_name: str = 'blog'

urlpatterns: List[Union[URLResolver, URLPattern]] = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]

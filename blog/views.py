from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Blog
from django.core.mail import send_mail
from online_store.settings import EMAIL_BACKEND
from typing import Optional, List, Dict, Any
from django.db.models.query import QuerySet


class BlogCreateView(CreateView):
    """
    Controller for creating a new blog article.
    """
    model: Blog = Blog
    fields: tuple[str, ...] = ('title', 'content', 'preview', 'is_published')
    success_url: str = reverse_lazy('blog:list')


class BlogListView(ListView):
    """
    Controller for displaying a list of published blog articles.
    """
    model = Blog

    def get_queryset(self) -> QuerySet[Blog]:
        """
        Returns only published articles.
        """
        # Get the base queryset
        queryset = super().get_queryset()
        # Filter by publication type
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    """
    Controller for viewing a single blog article.
    Increments the view counter and sends a notification when 100 views are reached.
    """
    model = Blog

    def get_object(self, queryset: Optional[QuerySet] = None) -> Blog:
        """
        Gets the article object, increments the view counter,
        sends an email when 100 views are reached, and returns the object.
        """
        self.object = super().get_object(queryset)
        # Increasing the view counter
        self.object.views_count += 1
        # We check whether the counter has reached exactly 100 on this viewing
        if self.object.views_count == 100:
            send_mail(
                subject='Поздравляем! Ваша статья очень популярна!',
                message=f'Ваша статья "{self.object.title}" достигла 100 просмотров!',
                from_email=EMAIL_BACKEND,
                recipient_list=['your_real_email@example.com']

            )
        # Save changes to the database
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    """
    Controller for editing an existing blog post.
    """
    model = Blog
    fields: tuple[str, ...] = ('title', 'content', 'preview', 'is_published')

    def get_success_url(self) -> str:
        """
        Returns the redirect URL after a successful article update.
        Redirects to the detailed view page for the same article.
        """
        # Dynamically generate a URL based on the pk of the edited object
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    """
    Controller for deleting a blog article.
    """
    model = Blog
    success_url: str = reverse_lazy('blog:list')

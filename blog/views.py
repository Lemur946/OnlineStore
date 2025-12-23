from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Blog
from django.core.mail import send_mail
from online_store.settings import EMAIL_BACKEND


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog:list')  # Redirect address after success


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        # Get the base queryset
        queryset = super().get_queryset()
        # Filter by publication type
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
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
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')

    def get_success_url(self):
        # Dynamically generate a URL based on the pk of the edited object
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')

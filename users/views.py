from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

from .forms import UserRegisterForm, UserProfileForm
from .models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # We are sending a registration confirmation email.
        user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией!',
            message='Вы успешно зарегистрировались в нашем онлайн магазине Skystore.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        # Гарантируем, что пользователь может редактировать только свой профиль
        return self.request.user

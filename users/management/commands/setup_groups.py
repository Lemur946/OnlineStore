from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product  # Убедитесь, что импортируете вашу модель Product


class Command(BaseCommand):
    """
    A command for creating and configuring user groups.
    """

    def handle(self, *args, **options):
        # --- Creating a "Product Moderator" group ---
        moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')
        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана.'))

        # Obtain the necessary rights
        try:
            # Right to cancel publication
            unpublish_perm = Permission.objects.get(codename='can_unpublish_product')

            # Standard right of deletion
            delete_perm = Permission.objects.get(codename='delete_product')

            # Adding rights to the group
            moderator_group.permissions.add(unpublish_perm, delete_perm)
            self.stdout.write(self.style.SUCCESS('Права "can_unpublish_product" и "delete_product" добавлены группе.'))

        except Permission.DoesNotExist:
            self.stdout.write(self.style.ERROR('Одно из разрешений не найдено. Выполнили миграции?'))

        # --- Создание группы "Контент-менеджер" (из доп. задания) ---
        # Если вы делаете доп. задание, можете добавить логику здесь.
        # content_manager_group, created = Group.objects.get_or_create(name='Контент-менеджер')
        # ... и так далее

        self.stdout.write(self.style.SUCCESS('Настройка групп успешно завершена.'))

import json
from typing import Any, Dict, List

from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    """
Command class for Django management.
"""
    help = 'Очищает и заполняет базу данных данными из фикстуры data.json'

    def handle(self, *args: Any, **options: Any) -> None:
        """
The main method of the command that executes all the logic.
        """
        # We start with products, as they link to categories
        self.stdout.write('Очистка базы данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('База данных успешно очищена.'))

        fixture_path = 'catalog/fixtures/data.json'
        try:
            with open(fixture_path, 'r', encoding='utf-8') as f:
                data: List[Dict[str, Any]] = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Файл фикстуры не найден: {fixture_path}'))
            return

        categories_to_create: List[Category] = []
        # Dictionary for mapping PK from fixture to category name
        pk_to_category_name_map: Dict[int, str] = {}

        for item in data:
            if item['model'] == 'catalog.category':
                fields = item['fields']
                categories_to_create.append(Category(**fields))
                # Save the category name using its old PK from the file
                pk_to_category_name_map[item['pk']] = fields['name']

        # Create all categories with one query to the database
        Category.objects.bulk_create(categories_to_create)
        self.stdout.write(self.style.SUCCESS(f'Успешно загружено {len(categories_to_create)} категорий.'))

        name_to_category_instance_map: Dict[str, Category] = {
            cat.name: cat for cat in Category.objects.all()
        }

        products_to_create: List[Product] = []
        for item in data:
            if item['model'] == 'catalog.product':
                fields = item['fields']
                category_pk_from_fixture = fields.pop('category')

                # Find the category name by its old PK
                category_name = pk_to_category_name_map.get(category_pk_from_fixture)

                if category_name:
                    # Get the actual category object from the DB by name
                    category_instance = name_to_category_instance_map.get(category_name)
                    if category_instance:
                        fields['category'] = category_instance
                        products_to_create.append(Product(**fields))

        # Create all products with one query to the database
        Product.objects.bulk_create(products_to_create)
        self.stdout.write(self.style.SUCCESS(f'Успешно загружено {len(products_to_create)} продуктов.'))
        self.stdout.write(self.style.SUCCESS('Заполнение базы данных завершено.'))

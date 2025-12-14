from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """
Product category model.

Defines the name and description for each category.
"""
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания') # Закомментировано, т.к. не требуется в задании

    def __str__(self) -> str:
        """
        Returns a string representation of the Category object.
        """
        return f'{self.name}'

    class Meta:
        """
        Inner class for configuring the Category model.
        """
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """
    Product model.

    Defines all product characteristics, including its relationship to the category.
    """
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение (превью)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self) -> str:
        """
        Returns a string representation of the Product object.
        """
        return f'{self.name} ({self.category})'

    class Meta:
        """
        Inner class for configuring the Product model.
        """
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

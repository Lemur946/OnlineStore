from django.db import models
from typing import Optional

NULLABLE: dict[str, bool] = {'blank': True, 'null': True}


class Blog(models.Model):
    """
    A model representing a blog post.
    """
    title: str = models.CharField(max_length=150, verbose_name='Заголовок')
    content: str = models.TextField(verbose_name='Содержимое')
    preview: Optional[str] = models.ImageField(upload_to='blog_previews/', verbose_name='Превью', **NULLABLE)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published: bool = models.BooleanField(default=False, verbose_name='Признак публикации')
    views_count: int = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self) -> str:
        """
        Returns a string representation of the article object.
        """
        return self.title

    class Meta:
        """
        Meta class for the Blog model.
        """
        verbose_name: str = 'Статья'
        verbose_name_plural: str = 'Статьи'

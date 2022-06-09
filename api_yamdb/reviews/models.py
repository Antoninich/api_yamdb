from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api_yamdb import settings
from core.models import BaseTextModel
from reviews.utils import validate_date

User = get_user_model()


class Category(models.Model):
    name = models.CharField('Название', max_length=256, unique=True)
    slug = models.SlugField('Слаг', unique=True)

    class Meta:
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=256, unique=True)
    slug = models.SlugField('Слаг', unique=True)

    class Meta:
        verbose_name = 'Жанр'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField('Название', max_length=256)
    year = models.IntegerField('Год', blank=True, validators=[validate_date])
    description = models.CharField('Описание', max_length=256, blank=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='categories',
        verbose_name='Категория'
    )
    genre = models.ManyToManyField(
        'Genre',
        through='GenreTitle',
        related_name='genre',
        verbose_name='Жанр'
    )

    class Meta:
        verbose_name = 'Произведение'
        constraints = [
            models.UniqueConstraint(
                name='unique_title',
                fields=('name', 'year'),
            ),
        ]

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title = models.ForeignKey(
        'Title',
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        'Genre',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Жанры Произведения'

    def __str__(self):
        return self.title


class Review(BaseTextModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )
    score = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='unique_author_title',
                fields=('author', 'title'),
            ),
        ]

    def __str__(self):
        return self.text


class Comment(BaseTextModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )

    def __str__(self):
        return self.text

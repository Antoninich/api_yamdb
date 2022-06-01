from django.db import models


class BaseTextModel(models.Model):
    """Абстрактная модель. Добавляет дату публикации."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        abstract = True

from django.test import TestCase

from reviews.models import Category, Genre, Title


class ModelsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='test_name',
            slug='test_slug',
        )
        cls.genre = Genre.objects.create(
            name='test_name',
            slug='test_slug',
        )
        cls.title = Title.objects.create(
            name='test_name',
            year='2022',
        )

    def test_category_models_create(self):
        s = Category.objects.all()[0]
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(s.name, 'test_name')
        self.assertEqual(s.slug, 'test_slug')

    def test_genre_models_create(self):
        s = Genre.objects.all()[0]
        self.assertEqual(Genre.objects.count(), 1)
        self.assertEqual(s.name, 'test_name')
        self.assertEqual(s.slug, 'test_slug')

    def test_title_models_create(self):
        s = Title.objects.all()[0]
        self.assertEqual(Title.objects.count(), 1)
        self.assertEqual(s.name, 'test_name')
        self.assertEqual(s.year, 2022)

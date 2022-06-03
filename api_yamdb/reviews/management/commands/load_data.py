from reviews.models import (Category, Genre, GenreTitle,
                            Title)
import os
from csv import DictReader

from django.core.management import BaseCommand
from api_yamdb.settings import STATICFILES_DIRS
from users.models import UserProfile

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

PATH = os.path.join(STATICFILES_DIRS[0], 'data/')


class Command(BaseCommand):
    help = "Loads data from users.csv"

    def handle(self, *args, **options):

        # if Category.objects.exists():
        #     print('users data already loaded...exiting.')
        #     print(ALREDY_LOADED_ERROR_MESSAGE)
        #     return

        print("Loading users data")

        users_file = 'category.csv'
        users_path = os.path.join(PATH, users_file)
        with open(users_path, newline='', encoding='utf-8') as file:
            data = DictReader(file)

            for row in data:
                category = Category(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug'],
                )
                category.save()

        users_file = 'genre.csv'
        users_path = os.path.join(PATH, users_file)
        with open(users_path, newline='', encoding='utf-8') as file:
            data = DictReader(file)

            for row in data:
                category = Genre(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug'],
                )
                category.save()

        users_file = 'titles.csv'
        users_path = os.path.join(PATH, users_file)
        with open(users_path, newline='', encoding='utf-8') as file:
            data = DictReader(file)

            for row in data:
                category_id = Category.objects.get(pk=row['category'])
                title = Title(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category=category_id,
                )
                title.save()

        users_file = 'genre_title.csv'
        users_path = os.path.join(PATH, users_file)
        with open(users_path, newline='', encoding='utf-8') as file:
            data = DictReader(file)

            for row in data:
                title_id = Title.objects.get(pk=row['title_id'])
                genre_id = Genre.objects.get(pk=row['genre_id'])
                genre_title = GenreTitle(
                    id=row['id'],
                    title=title_id,
                    genre=genre_id,
                )
                genre_title.save()

        USERS_CSV_FILE = 'users.csv'
        users_path = os.path.join(PATH, USERS_CSV_FILE)
        for row in DictReader(open(users_path)):
            user = UserProfile(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name'],
            )
            user.save()

import os
import json
from faker import Faker
from django.core.management import BaseCommand
from django.conf import settings
from django.core import management
from django.core.management.commands import loaddata
from articles.models import ArticleCategory

fake = Faker()
IMAGES = os.listdir(settings.IMAGES_DIR)


def build_instance(pk: int):
    return {
        "model": "articles.article",
        "pk": pk,
        "fields":{
            "title": fake.sentence(5),
            "category": fake.random_choices(ArticleCategory.choices, 1)[0][0],
            "content": "\n\n".join(fake.paragraph(35) for _ in range(fake.random_int(5, 15))),
            "image": fake.random_choices(IMAGES, 1)[0],
        }
    }


class Command(BaseCommand):

    def handle(self, *args, **options):
        file_path = os.path.join(
            settings.BASE_DIR, 'articles.json'
        )
        with open(file_path, 'w') as f:
            json.dump([build_instance(i) for i in range(1, 35)], f)
        management.call_command(loaddata.Command(), file_path, verbosity=0)
        os.remove(file_path)

import os
from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import Post, Category
from django.contrib.auth.models import User
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Generate dummy data for Posts'

    def handle(self, *args, **kwargs):
        fake = Faker()
        categories = Category.objects.all()
        users = User.objects.all()
        n= 120

        for _ in range(n):
            title = fake.sentence(nb_words=6) 
            content = fake.text(max_nb_chars=12000) 
            thumbnail = 'images/news_en_1920x1080_edkTimn.jpg'
            category = random.choice(categories) 
            author = random.choice(users) 
            publish_date = fake.date_time_this_year() 

            Post.objects.create(
                title=title,
                content=content,
                thumbnail=thumbnail,
                category=category,
                nview=random.randint(0, 1000),
                nlikes=random.randint(0, 500),
                author=author,
                publish_date=publish_date
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {n} dummy posts.'))

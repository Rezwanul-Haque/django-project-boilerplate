import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.development')

import django

django.setup()

import random
from your_app.models import AllModels
from faker import Faker

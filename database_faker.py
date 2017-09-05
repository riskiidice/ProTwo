import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from AppTwo.models import *
from faker import Faker

fakegen = Faker()

def add_user():

    fake_firstname = fakegen.first_name
    fake_lastname = fakegen.last_name
    fake_email   = fakegen.company_email
    usr = User.objects.get_or_create(first_name=fake_firstname, last_name=fake_lastname, email=fake_email)[0]
    usr.save()
    return usr

def populate(N=5):

    for entry in range(N):
        add_user()

if __name__ == '__main__':
    print("Populate Script!!")
    populate(20)
    print("Populating complete!!")

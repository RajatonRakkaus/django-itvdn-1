from django.shortcuts import render
from django.http import HttpResponse

from lesson_5.models import Flower, Bouquet, Client

from decimal import Decimal
from uuid import uuid4

from django.contrib.auth.models import User
from django.core.files import File


def create_flower(request):
    rose = Flower()
    rose.count = 5
    rose.description = "Spiky flowers"
    rose.can_use_in_bouquet = True
    rose.wiki_page = "https://wikipedia.org/"
    rose.name = "Rose"
    rose.save()
    return HttpResponse("Created!")


def create_client(request):

    Client.objects.create(**{
        'user': User.objects.get(pk=1),
        'email': 'admin@admin.com',
        'name': 'John',
        'invoice': File(open('django_itvdn/requirements.txt')),
        'user_uuid': uuid4(),
        'discount_size': Decimal('0.02'),
        'client_ip': '192.0.2.1',
    })
    return HttpResponse("Created!")


def get_flower(request):
    price = Bouquet.shop.get(pk=1).price
    

    return HttpResponse(price)

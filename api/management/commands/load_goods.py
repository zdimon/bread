# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from api.models import * 



class Command(BaseCommand):

    def handle(self, *args, **options):
        
        print 'start loading'
        Category.objects.all().delete()
        c1 = Category.objects.create(name=u'Хлебное меню')
        # c1 = Category(name=u'Хлебное меню').save()
        c2 = Category.objects.create(name=u'Кондитерские изделия')
        Category.objects.create(name=u'Багеты',parent=c1)
        Category.objects.create(name=u'Хлеб',parent=c1)
        Category.objects.create(name=u'Слойки',parent=c2)
        Category.objects.create(name=u'Пирожное',parent=c2)
        Category.objects.create(name=u'Булочки',parent=c2)
        Category.objects.create(name=u'Эклеры',parent=c2)
        Category.objects.create(name=u'Круасаны',parent=c2)
        Category.objects.create(name=u'Домашняя выпечка',parent=c2)
        print 'it is done'


       

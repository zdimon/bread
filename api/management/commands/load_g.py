# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from api.models import * 



class Command(BaseCommand):

    def handle(self, *args, **options):
        print 'start loading categories'
        Category.objects.all().delete()
        c1 = Category.objects.create(name=u'Хлебное меню')
        print 'ffff'
        c2 = Category.objects.create(name=u'Хлебное меню', parent=c1)

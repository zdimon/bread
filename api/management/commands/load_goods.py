# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from api.models import * 
from django.core.files import File
from bread.settings import BASE_DIR

class Command(BaseCommand):

    def handle(self, *args, **options):
        print 'start loading categories'
        Category.objects.all().delete()
        c1 = Category.objects.create(name=u'Хлебное меню')
        # c1 = Category(name=u'Хлебное меню').save()
        c2 = Category.objects.create(name=u'Кондитерские изделия')
        c3 = Category.objects.create(name=u'Багеты', parent=c1)
        c4 = Category.objects.create(name=u'Хлеб', parent=c1)
        c5 = Category.objects.create(name=u'Слойки', parent=c2)
        c6 = Category.objects.create(name=u'Пирожное', parent=c2)
        c7 = Category.objects.create(name=u'Булочки', parent=c2)
        c8 = Category.objects.create(name=u'Эклеры', parent=c2)
        c9 = Category.objects.create(name=u'Круасаны', parent=c2)
        c10 = Category.objects.create(name=u'Домашняя выпечка', parent=c2)
        print 'it is done'

    
        print 'start loading goods'
        Product.objects.all().delete()
        p = Product.objects.create(
            name = u'Хлеб Бородинский 460 гр.',
            price = 55,
            description = '''Состав продукта: Солод красный, кориандр молотый, мука ржаная, мука в/с, сахар, масло растительное, кориандр целый, закваска, соль, вода. ''',
            ammount = 10,
            rate = 1,
            category = c1,
            subcategory = c4
        )
        
        file_path = BASE_DIR+'/api/fixtures/bread.jpg'
        reopen = open(file_path, "rb")
        django_file = File(reopen)
        im = ProductImages()
        im.product = p
        im.is_main = True
        im.save()
        im.image.save('bread.jpg',django_file,save=True)    


        for i in range(3,10):
            cname = 'c%s' % i 
            p = Product.objects.create(
                name = u'Хлеб злаковый 550гр',
                price = 55,
                description = '''Состав продукта: Солод красный, кориандр молотый, мука ржаная, мука в/с, сахар, масло растительное, кориандр целый, закваска, соль, вода. ''',
                ammount = 5,
                rate = 1,
                category = c1,
                subcategory = eval(cname)
            )
            
            file_path = BASE_DIR+'/api/fixtures/bread.jpg'
            reopen = open(file_path, "rb")
            django_file = File(reopen)
            im = ProductImages()
            im.product = p
            im.is_main = True
            im.save()
            im.image.save('bread.jpg',django_file,save=True)   
   
        
        print 'it is done'

       

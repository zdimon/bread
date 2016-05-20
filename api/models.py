# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from image_cropping import ImageRatioField
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer
import pytils
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

class Kiosk(models.Model):
    u''' Класс Киоск содержит все данные о киоске (адрес, фото, мнемонику, широту, долготу) '''
    address = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='media', null=True, blank=True)
    cropping = ImageRatioField('foto', '430x360')
    mnemonic = models.CharField(max_length=5)
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=200)
    scheduler = models.CharField(max_length=200, default='с 9 до 6 в будни')
    pub = models.BooleanField(default=True, verbose_name=u'Опубликован?') 
    def __unicode__(self):
        return self.name

class Category(MPTTModel):
    ''' Класс категори товаров'''
    name = models.CharField(max_length=200)
    name_slug = models.CharField(verbose_name='Name slug',max_length=250, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    def get_absolute_url(self):
       return reverse("catalog_filter", kwargs={"slug": self.name_slug})
    def __unicode__(self):
        return self.name
    def save(self, **kwargs):
        if not self.id:
            self.name_slug = pytils.translit.slugify(self.name)
        return super(Category, self).save(**kwargs)


class Product(models.Model):
    u''' Класс Продукт содержит данные о товарах (имя, фото, цену, описание, наличие товара)'''
    __original_ammount = None

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self.__original_ammount = int(self.ammount)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u"Стоимость (руб)")
    description = models.CharField(max_length=200)
    ammount = models.PositiveSmallIntegerField(default=0) 
    rate = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Category, null=True, blank=True, related_name='category')
    subcategory = models.ForeignKey(Category, null=True, blank=True, related_name='subcategory')
    name_slug = models.CharField(verbose_name='Name slug',max_length=250, blank=True)
    @property
    def short_name(self):
        return ' '.join(self.name.split(' ')[0:3])
    @property
    def thumb(self):
        try:
            image = ProductImages.objects.get(is_main=True,product=self)
            thumbnail_url = get_thumbnailer(image.image).get_thumbnail({
                'size': (100, 100),
                'box': image.cropping,
                'crop': True,
                'detail': True,
            }).url
            return mark_safe(u'<img src="%s" />' % thumbnail_url)
        except:
            return 'no image'
    @property
    def thumb_big(self):
        try:
            image = ProductImages.objects.get(is_main=True,product=self)
            thumbnail_url = get_thumbnailer(image.image).get_thumbnail({
                'size': (203, 280),
                'box': image.cropping,
                'crop': True,
                'detail': True,
            }).url
            return mark_safe(u'<img src="%s" />' % thumbnail_url)
        except:
             return mark_safe(u'<img src="/static/main/images/default_cover/small.jpg">')

    def __unicode__(self):
        return self.name
    def save(self, **kwargs):
        if not self.id:
            self.name_slug = pytils.translit.slugify(self.name)
        return super(Product, self).save(**kwargs)
    @property
    def get_other_images_except_main(self):
        return ProductImages.objects.filter(is_main=False,product=self)



class ProductImages(models.Model):
    from easy_thumbnails.files import get_thumbnailer
    u''' картинки товаров '''
    product = models.ForeignKey('Product')
    image  = models.ImageField(upload_to='product', verbose_name=u'Изображение')
    cropping = ImageRatioField('image', '430x360')
    is_main = models.BooleanField(default=False) 
    @property
    def thumb(self):
        try:
            thumbnail_url = get_thumbnailer(self.image).get_thumbnail({
                'size': (100, 100),
                'box': self.cropping,
                'crop': True,
                'detail': True,
            }).url
            return mark_safe(u'<img src="%s" />' % thumbnail_url)
        except:
            return 'no image'
    def save(self, **kwargs):
        if not self.id:
            if not ProductImages.objects.filter(product=self.product).exists():
                self.is_main = True
        return super(ProductImages, self).save(**kwargs)


class Client(User):
    u''' Класс Клиент содержит данные о клиенте  '''
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'Имя')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'Телефон')
    created_at = models.DateTimeField(auto_now_add=True)
    kiosk = models.ForeignKey('Kiosk', null=True, blank=True)
    def __unicode__(self):
        return self.name


class Order(models.Model):
    u''' заказы по клиенту '''
    __original_status = None
    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self.__original_status = self.status
    STATUSES = (
        (1, u'Новый'),
        (2, u'Киоск выбран'),
        (3, u'Ожидает оплаты'),
        (4, u'Оплачен'),
        (5, u'Доставка'),
        (6, u'Доставлен'),
        (7, u'Отказ'),
    )

    status = models.IntegerField(verbose_name=u'Статус заказа' ,
                                    choices=STATUSES,
                                    default=1,
                                    )
    client = models.ForeignKey('Client', null=True, blank=True) 
    kiosk = models.ForeignKey('Kiosk', null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    session = models.CharField(max_length=250, null=True, blank=True)
    @property
    def total(self):
        t = 0
        for i in self.orderitem_set.all():
            t = t + (i.product.price*i.ammount)
        return t
    
    def save(self, **kwargs):
        #from mapshop.tasks import change_order_status_task
        if self.status != self.__original_status:
            #change_order_status_task.delay(self)
            self.__original_status = self.status
        return super(Order, self).save(**kwargs)

    def __unicode__(self):
        return u'Заказ № %s' % self.pk
    

class OrderItem(models.Model):
    u'''Элементы заказа'''
    order = models.ForeignKey('Order')
    product = models.ForeignKey('Product') 
    created_at = models.DateTimeField(auto_now_add=True)
    ammount = models.IntegerField(default=1)

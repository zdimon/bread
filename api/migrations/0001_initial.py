# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import django.contrib.auth.models
from django.conf import settings
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('name_slug', models.CharField(max_length=250, verbose_name='Name slug', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='api.Category', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u0418\u043c\u044f', blank=True)),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Kiosk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200)),
                ('foto', models.ImageField(null=True, upload_to='media', blank=True)),
                ('mnemonic', models.CharField(max_length=5)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('name', models.CharField(max_length=200)),
                ('scheduler', models.CharField(default='\u0441 9 \u0434\u043e 6 \u0432 \u0431\u0443\u0434\u043d\u0438', max_length=200)),
                ('pub', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d?')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430', choices=[(1, '\u041d\u043e\u0432\u044b\u0439'), (2, '\u041a\u0438\u043e\u0441\u043a \u0432\u044b\u0431\u0440\u0430\u043d'), (3, '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u043e\u043f\u043b\u0430\u0442\u044b'), (4, '\u041e\u043f\u043b\u0430\u0447\u0435\u043d'), (5, '\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430'), (6, '\u0414\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d'), (7, '\u041e\u0442\u043a\u0430\u0437')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('session', models.CharField(max_length=250, null=True, blank=True)),
                ('client', models.ForeignKey(blank=True, to='api.Client', null=True)),
                ('kiosk', models.ForeignKey(blank=True, to='api.Kiosk', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ammount', models.IntegerField(default=1)),
                ('order', models.ForeignKey(to='api.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c (\u0440\u0443\u0431)', max_digits=6, decimal_places=2)),
                ('description', models.CharField(max_length=200)),
                ('ammount', models.PositiveSmallIntegerField(default=0)),
                ('rate', models.PositiveSmallIntegerField(default=0)),
                ('name_slug', models.CharField(max_length=250, verbose_name='Name slug', blank=True)),
                ('category', models.ForeignKey(related_name='category', blank=True, to='api.Category', null=True)),
                ('subcategory', models.ForeignKey(related_name='subcategory', blank=True, to='api.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='product', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                (b'cropping', image_cropping.fields.ImageRatioField('image', '430x360', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                ('is_main', models.BooleanField(default=False)),
                ('product', models.ForeignKey(to='api.Product')),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(to='api.Product'),
        ),
        migrations.AddField(
            model_name='client',
            name='kiosk',
            field=models.ForeignKey(blank=True, to='api.Kiosk', null=True),
        ),
    ]

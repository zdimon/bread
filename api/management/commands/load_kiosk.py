# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from api.models import Kiosk 
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        print 'start'
        Kiosk.objects.all().delete()
        input_file = open("api/fixtures/kioski.csv", "rb")
        rdr = csv.DictReader(input_file, delimiter=';', fieldnames=['mnemonic', 'name', 'address','latitude','longitude'])
        for rec in rdr:
            #try:
            k = Kiosk()
            k.mnemonic = rec['mnemonic']
            k.name = rec['name']
            k.address = rec['address']
            k.latitude = rec['latitude']
            k.longitude = rec['longitude']
            k.save()
            print 'kiosk....%s...done' % k.address
        input_file.close()
        print 'done'


       

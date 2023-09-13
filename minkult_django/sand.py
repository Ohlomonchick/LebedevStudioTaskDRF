import os
import django
import csv

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minkult_django.settings')
# django.setup()
#
# from db_api.models import *

with open('../data/data-1-structure-1.csv', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    headers = next(spamreader)
    print(headers)

    for row in spamreader:
        if ";" in row[1] or ";" in row[3]:
            print(row[0])
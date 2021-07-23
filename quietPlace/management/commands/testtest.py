from django.core.management.base import BaseCommand
from quietPlace.models import Cafe
import openpyxl
import pandas as pd

wb = openpyxl.load_workbook('quietPlace/cafe.xlsx')
sheet = wb.active
df = pd.DataFrame(sheet.values)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(33):
            Cafe.objects.create(cafe_name=df[0][i], cafe_description=df[1][i], working_hour=df[2][i], working_detail=df[3][i], phone=df[4][i], address=df[5][i], region=df[6][i], category=df[7][i], short_description=df[8][i], chair=df[9][i], table=df[10][i], socket=df[11][i], bathroom=df[12][i], volume=df[13][i],
            place_size=df[14][i], discussion_room=df[15][i], booking_available=df[16][i])
        print(Cafe.objects.all())
        return
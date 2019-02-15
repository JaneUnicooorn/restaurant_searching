import csv
from .models import Restaurant

with open('places - 10.csv', 'r') as f:
    rows = list(csv.reader(f, delimiter=','))

    for row in rows[1:]:
        obj, created = Restaurant.objects.get_or_create(
            place_name=row[0],
            place_id=row[1],
            address=row[2],
            links_gm=row[3],
            phone=row[4],
            latitude=row[5],
            longitude=row[6],
            text=row[7],
            w_to=row[8],
            day=row[9],
            expire_date=row[10],
            priority=row[11],
            text_id=row[12],
            w_from=row[13],
            price=row[14],
        )

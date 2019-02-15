from django.db import models

class Restaurant(models.Model):
    place_name = models.CharField(max_length=50)
    place_id = models.CharField(max_length=50)
    address = models.TextField()
    links_gm = models.TextField()
    phone = models.PositiveIntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    text = models.TextField()
    w_to = models.TimeField()
    day = models.PositiveSmallIntegerField()
    expire_date = models.CharField(blank=True, max_length=50)
    priority = models.PositiveSmallIntegerField()
    text_id = models.CharField(max_length=50)
    w_from = models.TimeField()
    price = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.place_name




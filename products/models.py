from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):

    state_choice = (
        ('VIC', 'Victoria'),
        ('NSW', 'New South Wales'),
        ('SA', 'South Australia'),
        ('NT', 'Northern Territory'),
        ('ACT', 'Australian Capital Territory'),
        ('TAS', 'Tasmania'),
        ('QLD', 'Queensland'),
        ('WA', 'Western Australia'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )


    product_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100) 
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    product_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    product_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    product_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    product_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    product_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = models.CharField(choices=features_choices, max_length=100)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    
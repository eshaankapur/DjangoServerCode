from django.db import models

# Create your models here.

class restaurants(models.Model):
	restaurant_id = models.AutoField(primary_key=True)
	restaurant_name = models.CharField(max_length=30)
	opening_time = models.TimeField(default='0500')
	closing_time = models.TimeField(default='2300')
	type = models.CharField(max_length=15, default='Reservation')
	TYPE = ('Reservation','Waitlist')


class users(models.Model):
	username = models.CharField(max_length=30,primary_key=True)
	password = models.CharField(max_length=30, null = True)
	first_name = models.CharField(max_length=50, null = True)
	last_name = models.CharField(max_length=50, null = True)
	phone_number = models.CharField(max_length=13, null = True)

class reservations(models.Model):
	reservation_id = models.AutoField(primary_key=True)
	restaurant_id = models.ForeignKey(restaurants,on_delete=models.CASCADE)
	username = models.ForeignKey(users,on_delete=models.CASCADE)
	time = models.TimeField(default='0000')
	date = models.DateField(default='01/01/18')

class menu_items(models.Model):
	item_id = models.AutoField(primary_key=True)
	restaurant_id = models.ForeignKey(restaurants,on_delete=models.CASCADE)
	item_name = models.CharField(max_length=40)
	price = models.DecimalField(max_digits=7,decimal_places=2, default =0)


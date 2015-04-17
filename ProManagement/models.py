from django.db import models
from django.utils import timezone
# Create your models here.
class Category(models.Model):
	category_name = models.CharField(max_length=10)
	pub_date = models.DateTimeField('date published')

	def __str__(self):  
		return self.category_name

class Product(models.Model):
	category = models.ForeignKey(Category)
	product_name = models.CharField(max_length=20)
	price = models.IntegerField(default=0)
	quantity = models.IntegerField(default=0)

	def __str__(self):  
		return self.product_name
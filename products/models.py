from django.db import models

class Product(models.Model):
	title = models.CharField(max_length = 50)
	description = models.TextField()
	availability = models.BooleanField(default = True)
	dateadded = models.DateField(auto_now_add= True, auto_now= False)
	lastmodified = models.DateTimeField(auto_now_add = False , auto_now= True)
	productimage = models.ImageField( upload_to= '/products/image')


	def __str__(self):
		return self.title
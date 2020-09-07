from django.db import models

# Create your models here.
class Accounts(models.Model):
	email = models.URLField(max_length=255)
	title = models.CharField(max_length=255)
	display = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	owner = models.CharField(max_length=255)
	address = models.TextField(max_length=10000)
	number = models.IntegerField()
	desc = models.TextField(max_length=10000)
	whatsapp = models.TextField(max_length=255)
	twitter = models.TextField(max_length=255)
	instagram = models.TextField(max_length=255)
	facebook = models.TextField(max_length=255)
	imageone = models.ImageField(upload_to='pics')

	def __str__(self):
   	 return self.title + ' ' + self.display
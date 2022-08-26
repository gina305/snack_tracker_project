from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):

	# Define fields
	name = models.CharField(max_length=64)
	#purchaser= models.ForeignKey('self', on_delete=models.CASCADE)#Define one-to-mny relationship betweeen purchaser
	# and snacks.
	description = models.TextField(max_length=30)


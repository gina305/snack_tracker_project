from django.db import models
from django.contrib.auth import get_user_model

# Create a snack model
class Snack(models.Model):

	# Define fields
	name = models.CharField(max_length=64)
	purchaser= models.ForeignKey(get_user_model(),on_delete=models.CASCADE)#Define one-to-mny relationship betweeen
	# purchaser
	# and snacks. (model to relate to, what to do when the purchaser is delweted in the snack model
	description = models.TextField(max_length=30)


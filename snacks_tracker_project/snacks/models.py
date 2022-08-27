from django.db import models
from django.contrib.auth import get_user_model # returns registered user model

# Create a snack model
class Snack(models.Model):

	# Define fields/attributes
	name = models.CharField(max_length=64)
	purchaser= models.ForeignKey(get_user_model(),on_delete=models.CASCADE)#Define one-to-mny relationship betweeen
	# purchaser exists in another model whr we want to define a 1 to many relationship
	# and snacks. (model to relate to, what to do when the purchaser is delweted in the snack model-deleted purchaser
	# in other model removes it in every model
	description = models.TextField(max_length=30)

	def __str__(self):
		return self.name


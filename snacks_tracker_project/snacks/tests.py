from django.test import TestCase

# Test Snack pages
# NOTE make sure test extends TestCase instead of SimpleTestCase used in previous class.
# verify status code
# verify correct template use
# use url name instead of hard coded path
# TIP: django.urls.reverse will help with that.
# We can’t easily test SnackDetailView just yet.
# Can you figure out why?

import re
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

# Create your tests here.
class snacksTests(TestCase):

	def test_setup(self):
		purchaser = get_user_model().objects.create(username="bob", password="password")
		Snack.objects.create(name="Ice Cream", purchaser=purchaser)

	def test_detialpage_status(self):
		# Navigate to the home page an return the status code
		url = reverse('snack_detail', args=(1,))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_listpage_status(self):
		# Navigate to the home page and return the status code
		url = reverse('snack_list')
		response = self.client.get(url)
		print(response)
		self.assertEqual(response.status_code, 200)


	def test_snack_list_Url_template(self):
		url = reverse('snack_list')
		response = self.client.get(url)
		self.assertTemplateUsed(response, 'base.html')

	def test_detail_page_template(self):
		url = reverse('showDetailList', args=(1,))
		response = self.client.get(url)
		self.assertTemplateUsed(response, 'snack_detail.html')
		self.assertTemplateUsed(response, 'base.html')

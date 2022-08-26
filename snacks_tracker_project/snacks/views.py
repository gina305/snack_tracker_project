from django.shortcuts import render
from django.views.generic import ListView
# ListVeiw is used tio list based on a template
# Create your views here.
class SnackListView(ListView):
	template_name =  "snack_list.html"
	model = # associate a a model to this vie. Define


	1. Dfine Models in models.py



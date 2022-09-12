from django.shortcuts import render
from .models import Snack
from django.views.generic import ListView, DetailView
# ListVeiw is used to list based on a template
# Create your views by extending the ListView class




class SnackListView(ListView):
	template_name =  "snack_list.html"
	model = Snack# associate a a model to this vie.

class SnackDetailView(DetailView):
	template_name =  "snack_detail.html"
	model = Snack# associate model to this view. Define



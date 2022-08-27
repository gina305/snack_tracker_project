from django.urls import path
from .views import SnackListView, SnackDetailView #mport the views

urlpatterns = [
    path("",SnackListView.as_view(), name="snack_list"),

    #int reps primary key
    path("<int:pk>",SnackDetailView.as_view(), name="snack_detail")
    #home route
]


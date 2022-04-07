from html.entities import html5


from django.urls import path
from .views import *
app_name = "client"

urlpatterns = [
    path('', clients_list),
    path('<int:pk>/', client_details),
    path('create/', create_client),
]
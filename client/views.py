from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    client = models.Client.objects.all()
    context = {
        "clients": client
    }

    return render(request, "main.html", context)
    
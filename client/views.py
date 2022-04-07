from multiprocessing import context
from multiprocessing.connection import Client
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models
from .forms import *

# Create your views here.

def clients_list(request):
    client = models.Client.objects.all()
    context = {
        "clients": client
    }

    return render(request, "clients_list.html", context)

def home(request):
    client = models.Client.objects.all()
    context = {
        "clients": client
    }    
    return render(request, "main.html", context)

def table(request):
    client = models.Client.objects.all()
    context = {
        "clients": client
    }       
    return render(request, "table.html", context)
   
def client_details(request, pk):
    client = get_object_or_404(models.Client, id=pk)
    context = {
        "client": client
    }
    return render(request, "details.html", context)

def create_client(request):
    forms = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            order_name = form.cleaned_data['order_name']
            total = form.cleaned_data['total']
            seamstress = models.Seamstress.objects.first()
            models.Client.objects.create(
                first_name = first_name,
                second_name = second_name,
                order_name = order_name,
                total = total,
                seamstress = seamstress
            )

    context = {
        'forms': forms
    }
    return render(request, "html.html", context)

from django.contrib import admin
from django.urls import path, include
from client.views import home, table

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('table/', table),
    path('clients/', include('client.urls', namespace="client"))
]

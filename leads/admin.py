from atexit import register
from django.contrib import admin
from .models import * 
# Register your models here.

admin.site.register(Lead)
admin.site.register(User)
admin.site.register(Agent)

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, Contact
admin.site.register(Contact)
admin.site.register(Blog)

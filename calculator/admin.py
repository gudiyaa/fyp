from django.contrib import admin
from .models import Personal,Qualification,Research_Publications
# Register your models here.
admin.site.register(Personal)
admin.site.register(Qualification)
admin.site.register(Research_Publications)
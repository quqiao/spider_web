from django.contrib import admin
from spider_page import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Person)
from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Soru)
admin.site.register(Category)
admin.site.register(Yanit)
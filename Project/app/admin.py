from django.contrib import admin
from .models import Cards
# Register your models here.
class CardsAdmin(admin.ModelAdmin):
    list_display=['name','rate']

admin.site.register(Cards,CardsAdmin)
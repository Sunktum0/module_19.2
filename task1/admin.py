from django.contrib import admin
from .models import Buyer, Game

class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'age_limited')
    search_fields = ('title',)

admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Game, GameAdmin)

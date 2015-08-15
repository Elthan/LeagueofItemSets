from django.contrib import admin
from .models import PlayerItemSet, Item, ItemStat

# Register your models here.
class PlayerItemSet_Admin(admin.ModelAdmin):
	list_display = ['item_set_id', 'item_set_date']

class Item_Admin(admin.ModelAdmin):
	list_display = ['item_id', 'name', 'description']
	


admin.site.register(PlayerItemSet, PlayerItemSet_Admin)
admin.site.register(Item, Item_Admin)
admin.site.register(ItemStat)
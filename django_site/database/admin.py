from django.contrib import admin
from .models import PlayerItemSet, Item, ItemStat, Champion, ChampionStat, Version

# Register your models here.
class PlayerItemSet_Admin(admin.ModelAdmin):
	list_display = ['item_set_id', 'item_set_date']

class Item_Admin(admin.ModelAdmin):
	list_display = ['item_id', 'name']
	
class Champion_Admin(admin.ModelAdmin):
	list_display = ['champ_id', 'name']
	
class Version_Admin(admin.ModelAdmin):
	list_display = ['region', 'version']
	

	


admin.site.register(PlayerItemSet, PlayerItemSet_Admin)
admin.site.register(Item, Item_Admin)
admin.site.register(ItemStat)
admin.site.register(Champion, Champion_Admin)
admin.site.register(ChampionStat)
admin.site.register(Version, Version_Admin)
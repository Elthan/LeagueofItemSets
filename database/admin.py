from django.contrib import admin
from .models import PlayerItemSet, Item, ItemStat, Champion, ChampionStat, Version

# Register your models here.
class PlayerItemSetAdmin(admin.ModelAdmin):
	list_display = ['item_set_id', 'item_set_date']

class ItemAdmin(admin.ModelAdmin):
	list_display = ['item_id', 'name']
	
class ChampionAdmin(admin.ModelAdmin):
	list_display = ['champ_id', 'name']
	
class VersionAdmin(admin.ModelAdmin):
	list_display = ['region', 'version']
	

admin.site.register(PlayerItemSet, PlayerItemSetAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemStat)
admin.site.register(Champion, ChampionAdmin)
admin.site.register(ChampionStat)
admin.site.register(Version, VersionAdmin)

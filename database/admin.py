from django.contrib import admin
from .models import PlayerItemSet, Item, ItemStat, Champion, ChampionStat, Version

# Register your models here.
class PlayerItemSetAdmin(admin.ModelAdmin):
	list_display = ['ItemSetID', 'ItemSetDate']

class ItemAdmin(admin.ModelAdmin):
	list_display = ['ItemID', 'Name']
	
class ChampionAdmin(admin.ModelAdmin):
	list_display = ['ChampID', 'Name']
	
class VersionAdmin(admin.ModelAdmin):
	list_display = ['Region', 'Version']
	

admin.site.register(PlayerItemSet, PlayerItemSetAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemStat)
admin.site.register(Champion, ChampionAdmin)
admin.site.register(ChampionStat)
admin.site.register(Version, VersionAdmin)

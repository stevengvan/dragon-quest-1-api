from django.contrib import admin
from .models import *

class LocationAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'image']

admin.site.register(Location, LocationAdmin)


class ArmorAdmin(admin.ModelAdmin):
    fields = ['name', 'image', 'stat_modified', 'modifier', 'buy_price', 'sell_price', 'locations']

admin.site.register(Armor, ArmorAdmin)


class WeaponAdmin(admin.ModelAdmin):
    fields = ['name', 'image', 'stat_modified', 'modifier', 'buy_price', 'sell_price', 'locations']

admin.site.register(Weapon, WeaponAdmin)


class ShieldAdmin(admin.ModelAdmin):
    fields = ['name', 'image', 'stat_modified', 'modifier', 'buy_price', 'sell_price', 'locations']

admin.site.register(Shield, ShieldAdmin)


class SpellAdmin(admin.ModelAdmin):
    fields = ['name', 'level_learned', 'mp_cost', 'spell_type', 'effect']

admin.site.register(Spell, SpellAdmin)


class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'effect', 'buy_price', 'locations']

admin.site.register(Item, ItemAdmin)


class EnemyAdmin(admin.ModelAdmin):
    fields = ['image', 'name', 'areas', 'hit_points', 'attack_power', 'attack_speed', 'spells', 'defense', 'experience', 'gold']

admin.site.register(Enemy, EnemyAdmin)
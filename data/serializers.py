from rest_framework import serializers
from .models import *

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'description', 'image']

class ArmorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armor
        fields = ['id', 'name', 'image', 'stat_modified', 'modifier', 'buy_price', 'sell_price', 'locations']

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['id', 'name', 'image', 'stat_modified', 'modifier', 'buy_price', 'sell_price', 'locations']

class ShieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shield
        fields = ['id', 'name', 'image', 'stat_modified', 'modifier', 'buy_price', 'sell_price', 'locations']

class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = ['id', 'name', 'level_learned', 'mp_cost', 'spell_type', 'effect']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'effect', 'buy_price', 'locations']

class EnemySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enemy
        fields = ['id', 'image', 'name', 'areas', 'hit_points', 'attack_power', 'attack_speed', 'spells', 'defense', 'experience', 'gold']
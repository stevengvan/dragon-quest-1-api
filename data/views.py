from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class LocationView(APIView):
    def get(self, request, **kwargs):
        query = None
        if "town" in kwargs:
            query = Location.objects.get(id=kwargs["town"])
        else:
            query = Location.objects.all()
        serializer = LocationSerializer(query) if "town" in kwargs else LocationSerializer(query, many=True)
        return Response(serializer.data)

class ArmorView(APIView):
    def get(self, request, **kwargs):
        data = None
        # Grab data from specific armor
        if "type" in kwargs:
            armor_query = Armor.objects.get(id=kwargs["type"])
            armor_data = ArmorSerializer(armor_query).data
            if armor_data["buy_price"] == -1: armor_data["buy_price"] = "N/A"
            if armor_data["sell_price"] == -1: armor_data["sell_price"] = "N/A"
            armor_data["locations"] = armor_data["locations"].split(',')
            data = armor_data

        # Grab data for all armors
        else:
            armors_query = Armor.objects.all()
            armors_data = ArmorSerializer(armors_query, many=True).data

            # Go through each armor for their locations
            for i in range(0, len(armors_data)):
                if armors_data[i]["buy_price"] == -1: armors_data[i]["buy_price"] = "N/A"
                if armors_data[i]["sell_price"] == -1: armors_data[i]["sell_price"] = "N/A"
                armors_data[i]["locations"] = armors_data[i]["locations"].split(',')

            data = armors_data
        
        return Response(data)
    

class WeaponView(APIView):
    def get(self, request, **kwargs):
        data = None
        # Grab data from specific weapon
        if "type" in kwargs:
            weapon_query = Weapon.objects.get(id=kwargs["type"])
            weapon_data = WeaponSerializer(weapon_query).data
            if weapon_data["buy_price"] == -1: weapon_data["buy_price"] = "N/A"
            if weapon_data["sell_price"] == -1: weapon_data["sell_price"] = "N/A"
            weapon_data["locations"] = weapon_data["locations"].split(',')
            data = weapon_data

        # Grab data for all weapons
        else:
            weapons_query = Weapon.objects.all()
            weapons_data = WeaponSerializer(weapons_query, many=True).data

            # Go through each weapon for their locations
            for i in range(0, len(weapons_data)):
                if weapons_data[i]["buy_price"] == -1: weapons_data[i]["buy_price"] = "N/A"
                if weapons_data[i]["sell_price"] == -1: weapons_data[i]["sell_price"] = "N/A"
                weapons_data[i]["locations"] = weapons_data[i]["locations"].split(',')
            data = weapons_data
        
        return Response(data)
    

class ShieldView(APIView):
    def get(self, request, **kwargs):
        data = None
        # Grab data from specific shield
        if "type" in kwargs:
            shield_query = Shield.objects.get(id=kwargs["type"])
            shield_data = ShieldSerializer(shield_query).data
            shield_data["locations"] = shield_data["locations"].split(',')
            data = shield_data

        # Grab data for all shields
        else:
            shields_query = Shield.objects.all()
            shields_data = ShieldSerializer(shields_query, many=True).data

            # Go through each shield for their locations
            for i in range(0, len(shields_data)):
                if shields_data[i]["buy_price"] == -1: shields_data[i]["buy_price"] = "N/A"
                if shields_data[i]["sell_price"] == -1: shields_data[i]["sell_price"] = "N/A"
                shields_data[i]["locations"] = shields_data[i]["locations"].split(',')
            data = shields_data
        
        return Response(data)
    

class SpellView(APIView):
    def get(self, request, **kwargs):
        data = None
        # Grab data from specific spell
        if "type" in kwargs:
            spell_query = Spell.objects.get(id=kwargs["type"])
            spell_data = SpellSerializer(spell_query).data
            data = spell_data
        #Grab all spells
        else:
            spells_query = Spell.objects.all()
            spells_data = SpellSerializer(spells_query, many=True).data
            data = spells_data

        return Response(data)
    

class ItemView(APIView):
    def get(self, request, **kwargs):
        data = None
        # Grab data from specific item
        if "type" in kwargs:
            item_query = Item.objects.get(id=kwargs["type"])
            item_data = ItemSerializer(item_query).data
            item_data["locations"] = item_data["locations"].split(',')
            data = item_data

        # Grab data for all items
        else:
            items_query = Item.objects.all()
            items_data = ItemSerializer(items_query, many=True).data

            # Go through each item for their locations
            for i in range(0, len(items_data)):
                items_data[i]["locations"] = items_data[i]["locations"].split(',')
            data = items_data
        
        return Response(data)
    

class EnemyView(APIView):
    def get(self, request, **kwargs):
        data = None
        # Grab data from specific enemy
        if "type" in kwargs:
            enemy_query = Enemy.objects.get(id=kwargs["type"])
            enemy_data = EnemySerializer(enemy_query).data
            enemy_data["areas"] = enemy_data["areas"].split(',') if enemy_data["areas"] != None else []
            enemy_data["spells"] = enemy_data["spells"].split(',') if enemy_data["spells"] != None else []
            if enemy_data["attack_power"] == -1: enemy_data["attack_power"] = '?'
            if enemy_data["attack_speed"] == -1: enemy_data["attack_speed"] = '?'
            if enemy_data["defense"] == -1: enemy_data["defense"] = '?'
            if enemy_data["experience"] == -1: enemy_data["experience"] = 'NONE'
            if enemy_data["gold"] == -1: enemy_data["gold"] = 'NONE'
            data = enemy_data

        # Grab data for all enemies
        else:
            enemies_query = Enemy.objects.all()
            enemies_data = EnemySerializer(enemies_query, many=True).data

            # Go through each enemy for reformatting values
            for i in range(0, len(enemies_data)):
                enemies_data[i]["areas"] = enemies_data[i]["areas"].split(',') if enemies_data[i]["areas"] != None else []
                enemies_data[i]["spells"] = enemies_data[i]["spells"].split(',') if enemies_data[i]["spells"] != None else []
                if enemies_data[i]["attack_power"] == -1: enemies_data[i]["attack_power"] = '?'
                if enemies_data[i]["attack_speed"] == -1: enemies_data[i]["attack_speed"] = '?'
                if enemies_data[i]["defense"] == -1: enemies_data[i]["defense"] = '?'
                if enemies_data[i]["experience"] == -1: enemies_data[i]["experience"] = 'NONE'
                if enemies_data[i]["gold"] == -1: enemies_data[i]["gold"] = 'NONE'
            data = enemies_data
        
        return Response(data)
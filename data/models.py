from django.db import models
import uuid


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=600)
    image = models.URLField()

    def __str__(self):
        return self.name

class Armor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    image = models.URLField()
    stat_modified = models.CharField(max_length= 10, default="Defense")
    modifier = models.IntegerField()
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    locations = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Weapon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    image = models.URLField()
    stat_modified = models.CharField(max_length= 10, default="Offense")
    modifier = models.IntegerField()
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    locations = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Shield(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    image = models.URLField()
    stat_modified = models.CharField(max_length= 10, default="Defense")
    modifier = models.IntegerField()
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    locations = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Spell(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    level_learned = models.IntegerField()
    mp_cost = models.IntegerField()
    spell_type = models.CharField(max_length=10)
    effect = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    effect = models.CharField(max_length=100)
    buy_price = models.IntegerField()
    locations = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Enemy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.URLField()
    name = models.CharField(max_length=50)
    areas = models.CharField(max_length=120)
    hit_points = models.IntegerField()
    attack_power = models.IntegerField()
    attack_speed = models.IntegerField()
    spells = models.CharField(max_length=120, null=True, blank=True)
    defense = models.IntegerField()
    experience = models.IntegerField()
    gold = models.IntegerField()

    def __str__(self):
        return self.name

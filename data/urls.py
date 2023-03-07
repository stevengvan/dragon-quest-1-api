from django.urls import path
from .views import *

urlpatterns = [
    path("locations/all/", LocationView.as_view(), name="all locations"),
    path("locations/<uuid:town>/", LocationView.as_view(), name="get location"),
    path("armors/all/", ArmorView.as_view(), name="all armors"),
    path("armors/<uuid:type>/", ArmorView.as_view(), name="get armor"),
    path("weapons/all/", WeaponView.as_view(), name="all weapons"),
    path("weapons/<uuid:type>/", WeaponView.as_view(), name="get weapon"),
    path("shields/all/", ShieldView.as_view(), name="all shields"),
    path("shields/<uuid:type>/", ShieldView.as_view(), name="get shields"),
    path("spells/all/", SpellView.as_view(), name="all spells"),
    path("spells/<uuid:type>/", SpellView.as_view(), name="get spells"),
    path("items/all/", ItemView.as_view(), name="all items"),
    path("items/<uuid:type>/", ItemView.as_view(), name="get items"),
    path("enemies/all/", EnemyView.as_view(), name="all enemies"),
    path("enemies/<uuid:type>/", EnemyView.as_view(), name="get enemies"),
]

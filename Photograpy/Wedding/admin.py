from django.contrib import admin
from . models import Favourite, Ceremony, Engagement
# Register your models here.

admin.site.register(Favourite),
admin.site.register(Ceremony),
admin.site.register(Engagement),
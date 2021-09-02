from django.contrib import admin

from .models import People

# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
    pass

admin.site.register(People, PeopleAdmin)
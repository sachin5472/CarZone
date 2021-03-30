from django.contrib import admin
from .models import Team 
from django.utils.html import format_html
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" style="border-radius:50px;" width="40"/>'.format(object.photo.url))
    thumbnail.short_description='photo'

    list_display=('id','thumbnail','first_name','designation','created_date')
    list_display_links=('first_name','id','thumbnail',)
    search_fields=('first_name','last_name','designation')
    list_filter=('designation',)
admin.site.register(Team,TeamAdmin)
from django.contrib import admin

from artists.models import Artist, Board


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'serial_number', 'pinterest_page_url')}),
        ('Links', {'fields': (
            'artstation_url', 'behance_url', 'deviantart_url', 'facebook_url',
            'instagram_url', 'pinterest_url', 'pixiv_url', 'tumblr_url',
            'twitter_url', 'weibo_url', 'other_url',
        )}),
    )
    list_display = ['serial_number', 'name']
    ordering = ['serial_number']


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

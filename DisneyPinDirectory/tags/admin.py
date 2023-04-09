from django.contrib import admin
from django.utils.html import format_html

from tags.forms import TagForm
from tags.models import Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    form = TagForm
    list_display = ['name', 'category', 'color_hex']
    ordering = ['category']

    def color_hex(self, obj):
        return format_html(
            '<b style="background:{};">{}</b>',
            obj.color,
            obj.color,
        )

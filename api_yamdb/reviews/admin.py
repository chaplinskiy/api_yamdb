from django.contrib import admin

from .models import Categories, Genres


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    empty_value_display = '-пусто-'


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Genres, GenreAdmin)

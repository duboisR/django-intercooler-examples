from django.contrib import admin

from sortable_list.models import FavoriteColor


class FavoriteColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')


admin.site.register(FavoriteColor, FavoriteColorAdmin)

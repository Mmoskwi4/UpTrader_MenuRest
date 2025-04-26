from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    list_display = ('name',) # Поля для отображения в списке
    search_fields = ('name',)  # Добавляет поле для поиска


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('menu', 'title', 'parent', 'url', 'slug')  # Поля для отображения в списке
    list_filter = ('menu', 'parent',)  # Фильтры справа
    search_fields = ('menu', 'title', 'parent',)  # Добавляет поле для поиска
    ordering = ('title',) # сортировка по имени

    fieldsets = (  # Разбивает форму редактирования на секции
        (None, {
            'fields': ('menu', 'title', 'parent')
        }),
        ('Дополнительно', {
            'fields': ('url', 'slug'),
        }),
    )
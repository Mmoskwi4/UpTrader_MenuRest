from django.contrib import admin
from .models import FoodCategory, Food


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'order_id')  # Поля для отображения в списке
    list_editable = ('order_id',)  # Позволяет редактировать order_id прямо в списке
    search_fields = ('name_ru',)  # Добавляет поле для поиска
    ordering = ('order_id',)  # Сортировка по умолчанию


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'category', 'cost', 'is_publish', 'internal_code')  # Поля для отображения в списке
    list_filter = ('category', 'is_vegan', 'is_special', 'is_publish')  # Фильтры справа
    search_fields = ('name_ru', 'code', 'internal_code')  # Добавляет поле для поиска
    list_editable = ('is_publish',)  # Позволяет редактировать is_publish прямо в списке
    filter_horizontal = ('additional',)  # Для ManyToMany полей - более удобный виджет
    ordering = ('name_ru',) # сортировка по имени

    fieldsets = (  # Разбивает форму редактирования на секции
        (None, {
            'fields': ('category', 'name_ru', 'description_ru', 'description_en', 'description_ch', 'cost', 'is_publish')
        }),
        ('Дополнительно', {
            'fields': ('is_vegan', 'is_special', 'code', 'internal_code', 'additional'),
            'classes': ('collapse',)  # Скрывает секцию по умолчанию
        }),
    )
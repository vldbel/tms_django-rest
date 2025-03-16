from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'published_date', 'is_active')  # Поля, отображаемые в списке
    list_filter = ('is_active', 'year')  # Фильтры в боковой панели
    search_fields = ('title', 'author')  # Поля для поиска
    ordering = ('-published_date',)  # Сортировка по убыванию даты публикации

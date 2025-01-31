from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "availability", "publication_date")
    search_fields = ("title", "author", "genre")
    list_filter = ("availability", "genre")



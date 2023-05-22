from django.contrib import admin
from .models import Snippet, Language, Framework

# Register your models here.
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'framework',]
    list_filter = ['language', 'framework']
    search_fields = ['title', 'code', 'description']
    list_per_page = 10

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10

@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'language']
    list_filter = ['language']
    search_fields = ['name']
    list_per_page = 10

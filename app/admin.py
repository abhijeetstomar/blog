from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # list_display attribute specifies fields displayed in Post list page for every Post
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    
    list_filter = ('status', 'created', 'publish', 'author')

    # This will make a search bar appear on the page
    search_fields = ('title', 'body')
    
    # This will make the slug field fill automatically when 
    # the Title field is entered while creating a new Post
    prepopulated_fields = {'slug': ('title',)}
    
    raw_id_fields = ('author',)

    # This will make a date hierarchy navigation appear below the search bar
    date_hierarchy = 'publish'
    
    # Posts will be ordered by Status or Published columns by default
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)
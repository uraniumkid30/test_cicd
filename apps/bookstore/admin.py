from django.contrib import admin
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'category', 'approved')
   

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
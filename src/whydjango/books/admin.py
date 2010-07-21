from django.contrib import admin 

from whydjango.books.models import Book, BookOrderLink


class BookOrderLinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(BookOrderLink, BookOrderLinkAdmin)

class BookOrderLinkInline(admin.TabularInline):
    model = BookOrderLink

class BookAdmin(admin.ModelAdmin):
    inlines = [BookOrderLinkInline ,]
    
admin.site.register(Book, BookAdmin)

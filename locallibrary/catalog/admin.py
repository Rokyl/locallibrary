from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

class AuthorAdmin(admin.ModelAdmin):
    list_display =  ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
class BookAdmin(admin.ModelAdmin):
    pass
class BookInstanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author,AuthorAdmin)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Book)

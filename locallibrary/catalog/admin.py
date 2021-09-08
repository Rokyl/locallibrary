from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ('last_name', 'first_name', ('date_of_birth', 'date_of_death'))


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')


admin.site.register(Genre)
#admin.site.register(Book, BookAdmin)
#admin.site.register(Author, AuthorAdmin)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'id')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
class BookInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

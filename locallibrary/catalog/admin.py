from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(Book)
#admin.site.register(BookInstance)

# Define the Admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register Admin class with associated model
admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(BookInstance):
class BookInstanceAdmin(admin.ModelAdmin):
    pass
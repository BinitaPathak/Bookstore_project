from django.contrib import admin

from books.models import Book

# we need to tell the admin that Book objects have an admin interface.
# Register your models here.
admin.site.register(Book)

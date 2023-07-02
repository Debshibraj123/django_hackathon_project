from django.contrib import admin

from .models import Students, Book ,Book_Issue ,BookInstance

# Register your models here.
admin.site.register(Students)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Book_Issue)
from django.contrib import admin
from webapp.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['pk',  'created_at', 'status', 'edit_time']
    list_filter = [ 'status']
    fields = [ 'status',  'created_at',  'edit_time', 'name', 'email', 'text']




admin.site.register(Book, BookAdmin)

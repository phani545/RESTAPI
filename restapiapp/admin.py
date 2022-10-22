from atexit import register
from django.contrib import admin
from .models import Article
# Register your models here.

class postadmin(admin.ModelAdmin):
    list_display = ('id','title','author','email')
    list_display_links = ('title',)
    list_filter = ('date',)


admin.site.register(Article,postadmin)

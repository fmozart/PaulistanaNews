from django.contrib import admin
from newsapp.models import News, Category

class AdminNews(admin.ModelAdmin):
    list_display=('title','category','add_time')
admin.site.register(News,AdminNews)

class AdminCategory(admin.ModelAdmin):
    list_display = ('title', 'category_image')
admin.site.register(Category, AdminCategory)

from django.contrib import admin

from .models import Category_for_post, Country, Post, Tag_for_post

@admin.register(Category_for_post)
class CategoryForPostModelAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Country)
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_category', 'views_count')

    def get_category(self, obj):
        return obj.category_id.title
    
    
@admin.register(Tag_for_post)
class TagForPostModelAdmin(admin.ModelAdmin):
    list_display = ('title',)



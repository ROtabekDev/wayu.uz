from modeltranslation.translator import register, TranslationOptions
from .models import (
    Category_for_post, Country, Post, 
    Tag_for_post 
)

@register(Category_for_post)
class CategoryForPostTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Tag_for_post)
class TagForPostTranslationOptions(TranslationOptions):
    fields = ('title',)

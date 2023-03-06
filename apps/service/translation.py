from modeltranslation.translator import register, TranslationOptions
from .models import (
    Document_type, Category_for_event, 
    Event, Tag_for_QA, QA, Category_book,
    Language, Book
)

@register(Document_type)
class DocumentTypeTranslationOptions(TranslationOptions):
    fields = ('title', )
 

@register(Category_for_event)
class CategoryForEventTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'address', 'content')


@register(Tag_for_QA)
class TagForQATranslationOptions(TranslationOptions):
    fields = ('title',)


@register(QA)
class QATranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@register(Category_book)
class CategoryBookTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Book)
class QATranslationOptions(TranslationOptions):
    fields = ('title', 'author', 'description')
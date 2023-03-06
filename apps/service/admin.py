from django.contrib import admin

from .models import (
    Category_book,
    Language,
    Book,
    Category_for_event,
    Event,
    Tag_for_QA,
    QA,
    Document_type,
    International_document
)


@admin.register(Category_book)
class CategoryBookModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Language)
class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


@admin.register(Category_for_event)
class CategoryForEventModelAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Event)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'address')


@admin.register(Tag_for_QA)
class TagForQAModelAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(QA)
class QAModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


@admin.register(Document_type)
class DocumentTypeModelAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(International_document)
class InternationalDocumentModelAdmin(admin.ModelAdmin):
    list_display = ('get_country', 'get_document_type')

    def get_country(self, obj):
        return obj.country_id.name
    
    def get_document_type(self, obj):
        return obj.document_type.title

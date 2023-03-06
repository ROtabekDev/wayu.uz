from django.db import models

from helpers.models import BaseModel


class Category_book(BaseModel):
    """Kitoblar uchun toifalar modeli"""
    name = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Toifa'
        verbose_name_plural = 'Toifalar'


class Language(BaseModel):
    """Tillar"""
    title = models.CharField('Nomi', max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='Til'
        verbose_name_plural ='Tillar'


class Book(BaseModel):
    """Kitoblar uchun model"""
    title = models.CharField('Nomi', max_length=150)
    category_id = models.ForeignKey(Category_book, on_delete=models.SET_NULL, null=True)
    author = models.CharField('Muallif', max_length=100)
    year = models.DateField("Ishlab chiqarilgan yili")
    language_id = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    page_count = models.PositiveIntegerField("Sahifalar soni", default=1)
    description = models.TextField('Tavsifi')
    file = models.FileField('Fayl', upload_to='service/library/book/file/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='Kitob'
        verbose_name_plural ='Kitoblar'
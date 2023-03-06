from django.db import models

from helpers.models import BaseModel


class Category_for_event(BaseModel):
    """Tadbirlar uchun toifalar modeli"""
    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Tadbirlar uchun toifa'
        verbose_name_plural = 'Tadbirlar uchun toifalar'


class Event(BaseModel):
    """Tadbirlar uchun model"""
    title = models.CharField('Sarlavhasi', max_length=100)
    slug = models.SlugField('Slugi', max_length=100)
    slider = models.ImageField('Rasmi', upload_to='service/event/event/slider/')
    address = models.CharField('Manzili', max_length=150)
    category_id = models.ForeignKey(Category_for_event, on_delete=models.SET_NULL, null=True)
    content = models.TextField('Tadbir haqida ma`lumot')
    views_count = models.PositiveIntegerField('Ko`rishlar soni', default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Tadbir'
        verbose_name_plural = 'Tadbirlar'

    
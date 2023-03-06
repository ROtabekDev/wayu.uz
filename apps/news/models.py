from django.db import models

from helpers.models import BaseModel


class Category_for_post(BaseModel):
    """Toifalar uchun model""" 
    title = models.CharField('Nomi', max_length=100)
    slug = models.SlugField('Slugi', max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Toifa'
        verbose_name_plural = 'Toifalar'


class Country(BaseModel):
    "Mamlakatlar uchun model"
    name = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)
    flag = models.ImageField('Bayrog`i', upload_to='news/country/flags/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Mamlakat'
        verbose_name_plural = 'Mamlakatlar'


class Post(BaseModel):
    """Yangiliklar uchun model"""
    title = models.CharField('Sarlavhasi', max_length=250)
    slug = models.SlugField('Slugi', max_length=250)
    slider = models.ImageField('Rasmi', upload_to='news/post/slider/')
    category_id = models.ForeignKey(Category_for_post, on_delete=models.SET_NULL, verbose_name='Kategoriya', null=True)
    content = models.TextField('Maqola matni')
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name='Mamlakati', null=True)
    tags = models.ManyToManyField('Tag_for_post', verbose_name='Teglar')
    views_count = models.PositiveIntegerField('Ko`rishlar soni', default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'


class Tag_for_post(BaseModel):
    """Post uchun teglar"""
    title = models.CharField('Nomi', max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Teg'
        verbose_name_plural = 'Teglar'







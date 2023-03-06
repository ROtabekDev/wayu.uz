from django.db import models

from helpers.models import BaseModel


class Tag_for_QA(BaseModel):
    """Teglar uchun model"""
    title = models.CharField('Nomi', max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Teg'
        verbose_name_plural = 'Teglar'
    

class QA(BaseModel):
    """Savol va javoblar uchun model"""
    question = models.CharField('Savol', max_length=300)
    answer = models.CharField('Javob', max_length=300)
    tags = models.ManyToManyField(Tag_for_QA, verbose_name='Teglar')

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'Savol va javob'
        verbose_name_plural = 'Savol va javoblar'
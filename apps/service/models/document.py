from django.db import models

from helpers.models import BaseModel

from apps.news.models import Country


class Document_type(BaseModel):
    """Hujjat turlari uchun model"""
    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Hujjat turi'
        verbose_name_plural = 'Hujjat turlari'


class International_document(BaseModel):
    """Xalqaro hujjatlar"""
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    document_type = models.ForeignKey(Document_type, on_delete=models.SET_NULL, null=True)
    file = models.FileField('Fayl', upload_to='service/document/international_document/files/')

    def __str__(self):
        return f"{self.country_id.name} -> {self.document_type.title}"
    
    class Meta:
        verbose_name = 'Xalqaro hujjat'
        verbose_name_plural = 'Xalqaro hujjatlari'

    
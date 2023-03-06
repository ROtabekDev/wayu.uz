from django.db import models

from helpers.models import BaseModel


class Message(BaseModel):
    """Fikr-mulohazalar uchun model"""
    full_name = models.CharField('Ism, familiya', max_length=100)
    phone_number = models.CharField('Telefon raqam', max_length=20)
    email = models.EmailField('Elektron pochta', max_length=50)
    text = models.TextField('Xabar')

    def __str__(self):
        return self.full_name 
    
    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'


class Payment(BaseModel):
    """To`lovlar uchun model"""
    full_name = models.CharField('Ism, familiya', max_length=100)
    date = models.DateTimeField('Sanasi')
    amount = models.DecimalField('Pul miqdori', max_digits=12, decimal_places=2)
    
    def __str__(self):
        return self.full_name 
    
    class Meta:
        verbose_name = 'To`lov'
        verbose_name_plural = 'To`lovlar'


class Expense(BaseModel):
    """Xarajatlar uchun model"""
    amount = models.DecimalField('Pul miqdori', max_digits=12, decimal_places=2)
    date = models.DateTimeField('Sanasi')
    reason = models.CharField('Sababi', max_length=150)
    report = models.FileField('Hisoboti')
    
    def __str__(self):
        return self.reason 
    
    class Meta:
        verbose_name = 'Xarajat'
        verbose_name_plural = 'Xarajatlar'


class Useful_links(BaseModel):
    """Foydali havolalar uchun model"""
    title = models.CharField('Nomi', max_length=150)
    icon = models.ImageField('Rasmi', upload_to='main/useful_link/icon')
    link = models.URLField('Link', max_length=150)
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Foydali havola'
        verbose_name_plural = 'Foydali havolalar'


class Partner(BaseModel):
    """Hamkorlar uchun model"""

    PARTNER_TYPE = (
        ('State', 'Davlat'),
        ('Own', 'Xususiy')
    )

    title = models.CharField('Nomi', max_length=150)
    icon = models.ImageField('Rasmi', upload_to='main/partner/icon/')
    link = models.URLField('Link', max_length=150)
    type = models.CharField('Homiy turi', choices=PARTNER_TYPE, max_length=20)

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Hamkor'
        verbose_name_plural = 'Hamkorlar'
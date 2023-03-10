# Generated by Django 4.1.7 on 2023-03-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document_for_project',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='document_for_project',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='document_for_project',
            name='title_uz',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='document_type',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='document_type',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='document_type',
            name='title_uz',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='objective',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Maqsad matni'),
        ),
        migrations.AddField(
            model_name='objective',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Maqsad matni'),
        ),
        migrations.AddField(
            model_name='objective',
            name='text_uz',
            field=models.TextField(null=True, verbose_name='Maqsad matni'),
        ),
        migrations.AddField(
            model_name='objective',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='objective',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='objective',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Tavsifi'),
        ),
        migrations.AddField(
            model_name='project',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Tavsifi'),
        ),
        migrations.AddField(
            model_name='project',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Tavsifi'),
        ),
        migrations.AddField(
            model_name='project',
            name='short_description_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Qisqa tavsif'),
        ),
        migrations.AddField(
            model_name='project',
            name='short_description_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Qisqa tavsif'),
        ),
        migrations.AddField(
            model_name='project',
            name='short_description_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='Qisqa tavsif'),
        ),
        migrations.AddField(
            model_name='project',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='project',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='project',
            name='title_uz',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
    ]

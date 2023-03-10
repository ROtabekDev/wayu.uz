# Generated by Django 4.1.7 on 2023-03-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_for_post',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='category_for_post',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='category_for_post',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_uz',
            field=models.CharField(max_length=150, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Maqola matni'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='Maqola matni'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_uz',
            field=models.TextField(null=True, verbose_name='Maqola matni'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Sarlavhasi'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Sarlavhasi'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='Sarlavhasi'),
        ),
        migrations.AddField(
            model_name='tag_for_post',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='tag_for_post',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='tag_for_post',
            name='title_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='Nomi'),
        ),
    ]

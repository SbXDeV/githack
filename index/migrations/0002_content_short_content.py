# Generated by Django 4.0.2 on 2022-02-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='short_content',
            field=models.TextField(default=1, verbose_name='Короткое содержание поста'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.13 on 2024-07-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_alter_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='jpg_path',
            field=models.CharField(default='change', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='svg_path',
            field=models.CharField(default='change', max_length=200),
            preserve_default=False,
        ),
    ]
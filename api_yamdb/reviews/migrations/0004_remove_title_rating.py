# Generated by Django 2.2.16 on 2021-09-11 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_title_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
    ]

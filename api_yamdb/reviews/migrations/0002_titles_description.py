# Generated by Django 2.2.16 on 2021-09-09 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

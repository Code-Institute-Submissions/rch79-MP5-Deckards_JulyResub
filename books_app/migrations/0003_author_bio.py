# Generated by Django 3.2 on 2022-05-09 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0002_auto_20220509_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.2.1 on 2019-11-16 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleApi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='photo',
            new_name='photo_Url',
        ),
        migrations.AlterField(
            model_name='article',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

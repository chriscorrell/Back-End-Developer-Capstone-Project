# Generated by Django 4.2.1 on 2023-05-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_rename_name_menuitem_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
    ]

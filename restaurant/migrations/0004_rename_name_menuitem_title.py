# Generated by Django 4.2.1 on 2023-05-21 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_menuitem_delete_menu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='name',
            new_name='title',
        ),
    ]

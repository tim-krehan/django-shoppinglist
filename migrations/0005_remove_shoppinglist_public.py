# Generated by Django 3.2.5 on 2021-07-11 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0004_shoppinglist_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppinglist',
            name='public',
        ),
    ]

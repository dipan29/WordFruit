# Generated by Django 2.1.3 on 2019-02-02 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20190202_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='read',
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-13 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categories',
            new_name='name',
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-09 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0016_alter_forms_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forms',
            name='made_on',
        ),
        migrations.RemoveField(
            model_name='forms',
            name='receipt_id',
        ),
    ]

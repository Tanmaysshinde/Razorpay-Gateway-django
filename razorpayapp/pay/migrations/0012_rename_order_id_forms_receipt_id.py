# Generated by Django 3.2.4 on 2021-07-09 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0011_remove_forms_made_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forms',
            old_name='order_id',
            new_name='receipt_id',
        ),
    ]
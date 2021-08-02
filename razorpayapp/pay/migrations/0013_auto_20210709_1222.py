# Generated by Django 3.2.4 on 2021-07-09 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0012_rename_order_id_forms_receipt_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forms',
            name='id',
        ),
        migrations.AlterField(
            model_name='forms',
            name='receipt_id',
            field=models.CharField(blank=True, default=1, max_length=100, primary_key=1, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2.4 on 2021-07-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0014_auto_20210709_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='receipt_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]

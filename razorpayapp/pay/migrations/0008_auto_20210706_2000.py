# Generated by Django 3.2.4 on 2021-07-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0007_forms_made_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='made_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='forms',
            name='order_id',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]

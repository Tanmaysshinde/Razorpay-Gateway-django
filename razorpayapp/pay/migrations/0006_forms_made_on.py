# Generated by Django 3.2.4 on 2021-07-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0005_rename_payment_id_forms_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='made_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

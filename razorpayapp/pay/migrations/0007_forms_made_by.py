# Generated by Django 3.2.4 on 2021-07-06 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pay', '0006_forms_made_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='made_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='auth.user'),
            preserve_default=False,
        ),
    ]

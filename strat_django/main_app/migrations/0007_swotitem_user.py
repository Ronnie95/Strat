# Generated by Django 4.2.13 on 2025-01-03 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0006_swot_swotitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='swotitem',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='SwotItem', to=settings.AUTH_USER_MODEL),
        ),
    ]

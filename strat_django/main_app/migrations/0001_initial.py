# Generated by Django 4.2.13 on 2025-01-02 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('start_date', models.DateField()),
                ('progress', models.CharField(choices=[('Not started', 'Not started'), ('In Progress', 'In Progress'), ('On Hold', 'On Hold'), ('Complete', 'Complete')], default='not started', max_length=30)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KeyResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('target_value', models.FloatField()),
                ('current_value', models.FloatField()),
                ('deadline', models.DateField()),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='key_results', to='main_app.objective')),
            ],
        ),
    ]

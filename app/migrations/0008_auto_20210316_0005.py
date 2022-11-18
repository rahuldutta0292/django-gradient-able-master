# Generated by Django 2.2.10 on 2021-03-15 18:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210315_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemovement',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 16, 0, 5, 44, 680893)),
        ),
        migrations.AlterField(
            model_name='filemovement',
            name='section_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_section_from', to='app.Section'),
        ),
        migrations.AlterField(
            model_name='filemovement',
            name='section_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_section_to', to='app.Section'),
        ),
        migrations.AlterField(
            model_name='filemovement',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 16, 0, 5, 44, 680893)),
        ),
    ]
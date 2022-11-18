# Generated by Django 2.2.10 on 2021-03-15 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210315_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filemovement',
            old_name='section',
            new_name='section_from',
        ),
        migrations.RenameField(
            model_name='filemovement',
            old_name='put_up_before',
            new_name='section_to',
        ),
        migrations.AlterField(
            model_name='filemovement',
            name='puc',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.PUC'),
        ),
    ]
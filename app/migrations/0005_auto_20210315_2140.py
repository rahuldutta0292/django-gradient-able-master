# Generated by Django 2.2.10 on 2021-03-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210308_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemovement',
            name='remarks',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
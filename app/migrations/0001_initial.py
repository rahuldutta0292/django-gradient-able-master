# Generated by Django 4.1.3 on 2022-11-19 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatutoryDeposit',
            fields=[
                ('id', models.IntegerField(default='0', primary_key=True, serialize=False)),
                ('entry_date', models.DateField()),
                ('order_date', models.DateField()),
                ('mact_name', models.CharField(max_length=800)),
                ('mac_case_no', models.CharField(max_length=500)),
                ('party_name', models.CharField(max_length=500)),
                ('amount', models.CharField(max_length=500)),
                ('in_words', models.CharField(max_length=500)),
                ('cheque_no', models.CharField(max_length=100)),
                ('cheque_date', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.CharField(max_length=100)),
                ('order_date', models.CharField(max_length=100)),
                ('misc_case_no', models.CharField(max_length=500)),
                ('main_case_no', models.CharField(max_length=500)),
                ('appellant', models.CharField(max_length=500)),
                ('party_name', models.CharField(max_length=500)),
                ('amount', models.CharField(max_length=500)),
                ('in_words', models.CharField(max_length=1000)),
                ('cheque_no', models.CharField(max_length=100)),
                ('cheque_date', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
    ]

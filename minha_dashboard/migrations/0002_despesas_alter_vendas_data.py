# Generated by Django 4.1.5 on 2023-02-17 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minha_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_despesa', models.CharField(max_length=50)),
                ('total', models.FloatField()),
                ('data', models.DateField(default=datetime.datetime(2023, 2, 17, 8, 0, 56, 501603))),
            ],
        ),
        migrations.AlterField(
            model_name='vendas',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 2, 17, 8, 0, 56, 500935)),
        ),
    ]

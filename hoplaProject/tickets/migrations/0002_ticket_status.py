# Generated by Django 4.2.11 on 2024-04-17 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(default='Pendiente', max_length=25),
        ),
    ]

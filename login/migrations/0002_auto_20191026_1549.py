# Generated by Django 2.2.5 on 2019-10-26 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='place',
            field=models.CharField(choices=[('Auditorium', 'Auditorium'), ('Place2', 'Place2'), ('Place3', 'Place3')], default=[('Auditorium', 'Auditorium')], max_length=100),
        ),
    ]

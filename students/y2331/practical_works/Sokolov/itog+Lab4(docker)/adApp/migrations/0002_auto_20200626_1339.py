# Generated by Django 3.0.3 on 2020-06-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adbreak',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата показа'),
        ),
    ]

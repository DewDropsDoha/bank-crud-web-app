# Generated by Django 2.2 on 2021-09-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20210928_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(verbose_name='Enter Amount'),
        ),
    ]

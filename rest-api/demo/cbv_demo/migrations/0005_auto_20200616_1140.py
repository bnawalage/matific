# Generated by Django 3.0.7 on 2020-06-16 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbv_demo', '0004_auto_20200616_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerattempts',
            name='score',
            field=models.SmallIntegerField(),
        ),
    ]

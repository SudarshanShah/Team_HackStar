# Generated by Django 3.0.7 on 2020-12-17 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackstar', '0002_auto_20201217_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanliness_model',
            name='class_no',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cleanliness_model',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cleanliness_model',
            name='pnr',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='lost_found_model',
            name='class_no',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='lost_found_model',
            name='item',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='lost_found_model',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='lost_found_model',
            name='pnr',
            field=models.CharField(default='', max_length=100),
        ),
    ]

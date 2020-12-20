# Generated by Django 3.0.7 on 2020-12-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cleanliness_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10)),
                ('pnr', models.IntegerField(default=0)),
                ('building_name', models.CharField(default='', max_length=100)),
                ('class_no', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=100)),
            ],
        ),
    ]

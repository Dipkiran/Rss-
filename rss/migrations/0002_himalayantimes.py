# Generated by Django 2.0.5 on 2018-05-22 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HimalayanTimes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=120)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=120)),
                ('link', models.CharField(max_length=120)),
                ('Source', models.CharField(default='HimalayanTimes', max_length=120)),
            ],
        ),
    ]

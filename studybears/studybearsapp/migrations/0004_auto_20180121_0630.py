# Generated by Django 2.0.1 on 2018-01-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybearsapp', '0003_auto_20180120_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_classes', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='location',
            name='x_coordinate',
        ),
        migrations.RemoveField(
            model_name='location',
            name='y_coordinate',
        ),
        migrations.AddField(
            model_name='studygroups',
            name='date_times',
            field=models.ManyToManyField(to='studybearsapp.Date_And_Time'),
        ),
        migrations.AlterField(
            model_name='date_and_time',
            name='date_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='my_classes',
            field=models.ManyToManyField(to='studybearsapp.Classes'),
        ),
    ]

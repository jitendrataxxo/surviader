# Generated by Django 2.2.3 on 2019-07-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('work', models.CharField(max_length=50)),
                ('fnlwgt', models.IntegerField()),
                ('education', models.CharField(max_length=50)),
                ('education_num', models.IntegerField()),
                ('marital_status', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('relationship', models.CharField(max_length=50)),
                ('race', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('capital_gain', models.IntegerField()),
                ('capital_loss', models.IntegerField()),
                ('hours_per_week', models.IntegerField()),
                ('native_country', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=50)),
            ],
        ),
    ]

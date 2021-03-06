# Generated by Django 3.0.8 on 2020-07-11 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=17)),
                ('base_discount_percent', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'products',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
            ],
            options={
                'db_table': 'users',
                'ordering': ('first_name',),
            },
        ),
    ]

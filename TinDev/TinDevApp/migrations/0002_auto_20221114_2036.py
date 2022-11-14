# Generated by Django 3.2.13 on 2022-11-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TinDevApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('years', models.IntegerField()),
                ('zipcode', models.IntegerField()),
                ('skills', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]

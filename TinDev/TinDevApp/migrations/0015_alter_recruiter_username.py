# Generated by Django 4.1.3 on 2022-12-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TinDevApp", "0014_application_offer_expire"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recruiter",
            name="username",
            field=models.CharField(max_length=30, unique=True),
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("url", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urldata",
            name="slug",
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name="urldata",
            name="url",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

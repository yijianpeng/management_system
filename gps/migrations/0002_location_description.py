# Generated by Django 4.1.7 on 2023-03-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gps", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="description",
            field=models.TextField(default=12),
            preserve_default=False,
        ),
    ]

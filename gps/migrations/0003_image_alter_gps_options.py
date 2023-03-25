# Generated by Django 4.1.7 on 2023-03-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gps", "0002_remove_gps_time_gps_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
        migrations.AlterModelOptions(
            name="gps",
            options={"verbose_name": "GPS定位", "verbose_name_plural": "GPS定位"},
        ),
    ]

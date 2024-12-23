# Generated by Django 5.1.2 on 2024-11-28 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("musician", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Album",
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
                ("name", models.CharField(max_length=200)),
                ("release_date", models.DateField()),
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            (1, "1 - Star"),
                            (2, "2 - Star"),
                            (3, "3 - Star"),
                            (4, "4 - Star"),
                            (5, "5 - Star"),
                        ]
                    ),
                ),
                (
                    "musician",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="musician.musician",
                    ),
                ),
            ],
        ),
    ]

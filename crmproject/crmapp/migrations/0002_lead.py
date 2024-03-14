# Generated by Django 5.0.3 on 2024-03-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crmapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lead",
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
                ("name", models.CharField(max_length=100)),
                ("company", models.CharField(max_length=100)),
                ("email_id", models.EmailField(max_length=254)),
                ("mobile_number", models.CharField(max_length=15)),
                ("about", models.TextField()),
            ],
        ),
    ]

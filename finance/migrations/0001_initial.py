# Generated by Django 5.1.1 on 2024-10-22 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StockData",
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
                ("symbol", models.CharField(max_length=10)),
                ("date", models.DateField()),
                ("open_price", models.FloatField()),
                ("close_price", models.FloatField()),
                ("high_price", models.FloatField()),
                ("low_price", models.FloatField()),
                ("volume", models.BigIntegerField()),
            ],
            options={
                "unique_together": {("symbol", "date")},
            },
        ),
    ]

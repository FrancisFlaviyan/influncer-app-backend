# Generated by Django 4.2.6 on 2023-11-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "influencer_app",
            "0009_remove_campaign_brand_remove_engagement_brand_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="AllData",
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
                ("brand_name", models.CharField(max_length=100)),
                (
                    "brand_product",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("campaign_name", models.CharField(max_length=100)),
                (
                    "campaign_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("campaign_start_date", models.DateField(blank=True, null=True)),
                ("campaign_end_date", models.DateField(blank=True, null=True)),
                ("engagement_notes", models.TextField(blank=True, null=True)),
                (
                    "income_statement_last_payment",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "income_statement_income",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Brand",
        ),
        migrations.DeleteModel(
            name="Campaign",
        ),
        migrations.DeleteModel(
            name="Engagement",
        ),
        migrations.DeleteModel(
            name="IncomeStatement",
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-08 05:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("influencer_app", "0006_alter_brand_name_alter_campaign_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="is_auto_generated",
            field=models.BooleanField(default=False),
        ),
    ]

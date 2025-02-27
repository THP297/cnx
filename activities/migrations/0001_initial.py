# Generated by Django 4.2.17 on 2025-02-19 14:45

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Activities",
            fields=[
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_by", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "modified_by",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "contract_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("call_id", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "customer_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("agent", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "contacted_person",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "action_code",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("note", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Activity",
                "verbose_name_plural": "Activities",
            },
        ),
    ]

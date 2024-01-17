# Generated by Django 4.1.1 on 2022-09-19 19:41

from django.db import migrations, models
import django.db.models.deletion
import uuid
import wagtail.fields as wagtail_fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "test_charfield",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=255,
                        null=True,
                        verbose_name="char field",
                    ),
                ),
                ("test_textfield", models.TextField(blank=True)),
                ("test_richtextfield", wagtail_fields.RichTextField(blank=True)),
                (
                    "test_synchronized_charfield",
                    models.CharField(blank=True, max_length=255),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="TestSnippet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "translation_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                ("field", models.TextField(verbose_name="field")),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
        ),
    ]

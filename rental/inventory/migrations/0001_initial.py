# Generated by Django 4.1.4 on 2022-12-08 12:32

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(
                        help_text="format: required, max-100",
                        max_length=100,
                        verbose_name="category name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="format: required, letters, numbers, underscore, or hyphens",
                        max_length=150,
                        verbose_name="category safe URL",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        help_text="format: not required",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="children",
                        to="inventory.category",
                        verbose_name="parent of category",
                    ),
                ),
            ],
            options={
                "verbose_name": "product category",
                "verbose_name_plural": "product categories",
            },
        ),
    ]

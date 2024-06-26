# Generated by Django 5.0.6 on 2024-06-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0002_link_remove_project_url_project_links"),
    ]

    operations = [
        migrations.CreateModel(
            name="Technologies",
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
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="technologies",
            field=models.ManyToManyField(
                related_name="projects", to="portfolio.technologies"
            ),
        ),
    ]

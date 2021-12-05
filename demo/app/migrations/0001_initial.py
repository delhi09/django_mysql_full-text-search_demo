# Generated by Django 3.2.9 on 2021-12-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Novel",
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
                ("title", models.CharField(max_length=128)),
                ("author_name", models.CharField(max_length=64)),
                ("content", models.TextField()),
                ("search_text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "novel",
            },
        ),
        migrations.RunSQL(
            "CREATE FULLTEXT INDEX search_text_fulltext_search_index"
            " ON novel (search_text)"
            " WITH PARSER ngram",
            "DROP INDEX search_text_fulltext_search_index ON novel",
        ),
    ]
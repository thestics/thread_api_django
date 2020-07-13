# Generated by Django 3.0.8 on 2020-07-12 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=512)),
                ("link", models.CharField(max_length=4096)),
                ("author", models.CharField(max_length=128)),
                ("created_date", models.DateTimeField(auto_now=True)),
                ("up_votes", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("author", models.CharField(max_length=128)),
                ("created_date", models.DateTimeField(auto_now=True)),
                ("content", models.CharField(max_length=65536)),
                (
                    "related_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="thread_.Post"
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-07 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_delete_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="posts/"),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, choices=[('red', 'Red color'), ('green', 'Green color'), ('white', 'White color')], max_length=200, null=True),
        ),
    ]

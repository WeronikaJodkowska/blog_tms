# Generated by Django 4.0.6 on 2022-09-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congenial_bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender_name',
        ),
        migrations.AddField(
            model_name='message',
            name='action',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='message',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
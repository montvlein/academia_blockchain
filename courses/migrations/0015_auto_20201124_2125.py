# Generated by Django 3.0.4 on 2020-11-24 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_bookmark_deleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='user_awarded',
            new_name='user',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='certificate_requested',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
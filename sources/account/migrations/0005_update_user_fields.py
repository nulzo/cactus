# Generated by Django 4.2.4 on 2023-08-08 06:37

from django.db import migrations, models

import sources.account.models.user_account


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0004_alter_dailyspending_alcohol_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="profile_picture",
            field=models.ImageField(
                default="build/profile_pictures/default_pfp.jpg",
                upload_to=sources.account.models.user_account.image_path,
            ),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="sex",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("F", "Female"), ("NA", "Other")],
                max_length=2,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="theme",
            field=models.CharField(
                blank=True,
                choices=[("D", "Dark"), ("L", "Light")],
                default="D",
                max_length=1,
                null=True,
            ),
        ),
    ]

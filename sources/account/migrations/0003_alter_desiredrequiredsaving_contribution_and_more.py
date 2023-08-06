# Generated by Django 4.2.4 on 2023-08-06 02:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_alter_desiredrequiredsaving_required"),
    ]

    operations = [
        migrations.AlterField(
            model_name="desiredrequiredsaving",
            name="contribution",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="desiredrequiredsaving",
            name="loans",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="desiredrequiredsaving",
            name="nonrequired",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="desiredrequiredsaving",
            name="other",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="desiredrequiredsaving",
            name="saving",
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 4.0.1 on 2022-02-06 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_tbnotafiscal_idnfe'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbnotafiscal',
            name='flCancelada',
            field=models.BinaryField(null=True),
        ),
    ]

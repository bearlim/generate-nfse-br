# Generated by Django 4.0.1 on 2022-01-25 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_tbnotafiscal_idnfe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbnotafiscal',
            name='idNFE',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
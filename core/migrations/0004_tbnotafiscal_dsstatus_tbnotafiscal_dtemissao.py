# Generated by Django 4.0.1 on 2022-01-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tbnotafiscal_urlpdf_tbnotafiscal_urlxml'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbnotafiscal',
            name='dsStatus',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tbnotafiscal',
            name='dtEmissao',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

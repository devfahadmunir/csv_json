# Generated by Django 3.2.4 on 2021-06-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcsv', '0005_auto_20210615_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvdata',
            name='json_data',
            field=models.TextField(null=True),
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180525_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='key',
            field=models.CharField(max_length=255),
        ),
    ]
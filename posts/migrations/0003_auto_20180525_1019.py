# Generated by Django 2.0.5 on 2018-05-25 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180525_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Bio',
        ),
    ]

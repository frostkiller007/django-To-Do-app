# Generated by Django 2.2 on 2019-10-19 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20191019_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

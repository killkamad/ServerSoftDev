# Generated by Django 2.1.5 on 2019-02-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almau', '0002_auto_20190218_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='groups',
            field=models.ManyToManyField(to='almau.Group'),
        ),
    ]

# Generated by Django 2.0.1 on 2018-01-19 10:52

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180118_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
# Generated by Django 3.0.5 on 2020-04-28 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dm', '0002_auto_20200428_0428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'ordering': ['-timestamp']},
        ),
    ]

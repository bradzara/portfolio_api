# Generated by Django 5.1 on 2024-08-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

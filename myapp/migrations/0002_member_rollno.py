# Generated by Django 5.0 on 2024-01-10 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='rollno',
            field=models.IntegerField(null=True),
        ),
    ]
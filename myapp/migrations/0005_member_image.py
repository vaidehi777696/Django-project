# Generated by Django 5.0 on 2024-01-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_mobailno_member_phoneno'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='member_photo/'),
        ),
    ]
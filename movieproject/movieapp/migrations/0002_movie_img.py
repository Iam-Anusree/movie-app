# Generated by Django 4.2 on 2023-05-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='abcdef', upload_to='pictures'),
            preserve_default=False,
        ),
    ]

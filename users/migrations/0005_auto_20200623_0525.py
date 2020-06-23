# Generated by Django 2.2.5 on 2020-06-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200623_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'USD'), ('krw', 'KRW'), ('jpn', 'JPN')], max_length=3),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('jp', 'japanese'), ('ko', 'korean')], max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='superhost',
            field=models.BooleanField(default=False),
        ),
    ]
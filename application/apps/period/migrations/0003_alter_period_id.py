# Generated by Django 4.2.10 on 2024-04-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('period', '0002_auto_20240402_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

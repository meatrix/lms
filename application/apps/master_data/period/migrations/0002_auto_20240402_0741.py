# Generated by Django 3.1.5 on 2024-04-02 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
# Generated by Django 3.2.9 on 2023-12-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_news_rand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
# Generated by Django 4.2.6 on 2023-10-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConectaPlusapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
    ]
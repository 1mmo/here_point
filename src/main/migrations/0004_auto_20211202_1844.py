# Generated by Django 3.2.8 on 2021-12-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_advuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='category',
        ),
        migrations.AddField(
            model_name='place',
            name='category',
            field=models.ManyToManyField(to='main.Category'),
        ),
    ]

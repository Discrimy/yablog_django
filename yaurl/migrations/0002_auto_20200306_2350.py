# Generated by Django 3.0.3 on 2020-03-06 20:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('yaurl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortedurl',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='shortedurl',
            name='redirects',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.0.4 on 2020-05-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider_page', '0006_auto_20200518_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='mail',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='psw',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]

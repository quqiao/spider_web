# Generated by Django 3.0.4 on 2020-04-21 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='longyitjzq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cj', models.CharField(max_length=40)),
                ('gg', models.CharField(max_length=20)),
                ('xq', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('price2', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'longyi_tjzq',
                'managed': True,
            },
        ),
    ]

# Generated by Django 4.1 on 2022-09-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamapp', '0008_appliedjobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newstext', models.TextField()),
                ('newsdate', models.CharField(max_length=30)),
            ],
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('color', models.CharField(max_length=7)),
                ('rating', models.IntegerField()),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]

# Generated by Django 3.2.19 on 2023-06-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('ingredients', models.TextField()),
                ('servings', models.PositiveIntegerField()),
                ('prep_time', models.PositiveIntegerField()),
                ('instructions', models.TextField()),
            ],
        ),
    ]

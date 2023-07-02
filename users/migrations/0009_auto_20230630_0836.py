# Generated by Django 3.2.19 on 2023-06-30 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_organiser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_image',
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default=''),
        ),
    ]

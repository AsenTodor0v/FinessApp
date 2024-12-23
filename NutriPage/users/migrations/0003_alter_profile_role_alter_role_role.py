# Generated by Django 5.1.4 on 2024-12-07 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('User', 'User'), ('Nutritionist', 'Nutritionist'), ('Coach', 'Coach')], default='User', max_length=20),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(choices=[('Moderator', 'Moderator'), ('Staff', 'Staff'), ('Superuser', 'Superuser')], max_length=20),
        ),
    ]

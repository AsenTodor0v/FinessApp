# Generated by Django 5.1.4 on 2024-12-05 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0008_alter_savedmeals_unique_together_and_more'),
        ('users', '0002_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]

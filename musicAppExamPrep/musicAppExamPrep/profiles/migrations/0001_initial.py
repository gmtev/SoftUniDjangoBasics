# Generated by Django 4.2.16 on 2024-10-22 14:10

import django.core.validators
from django.db import migrations, models
import musicAppExamPrep.profiles.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), musicAppExamPrep.profiles.validators.UsernameValidator()])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
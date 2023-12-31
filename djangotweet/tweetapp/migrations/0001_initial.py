# Generated by Django 4.2.4 on 2023-08-27 16:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(50)])),
                ('message', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(150)])),
            ],
        ),
    ]

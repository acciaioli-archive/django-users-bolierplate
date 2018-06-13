# Generated by Django 2.0.1 on 2018-04-01 22:03

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import users.managers
import utils.models.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator(), utils.models.validators.BlackListValidator(['me'], 'Username not allowed.')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]
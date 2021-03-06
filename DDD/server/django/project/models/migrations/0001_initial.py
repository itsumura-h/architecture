# Generated by Django 2.2.7 on 2019-12-04 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '権限',
                'db_table': 'auth',
            },
        ),
        migrations.CreateModel(
            name='Nim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'nim',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('auth', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.Auth')),
            ],
            options={
                'verbose_name': 'ユーザー',
                'db_table': 'users',
            },
        ),
    ]

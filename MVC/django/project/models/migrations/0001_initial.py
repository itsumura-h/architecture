# Generated by Django 3.0.3 on 2020-02-21 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'ユーザー',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='MicroPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=140)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.User')),
            ],
            options={
                'verbose_name': '投稿',
                'db_table': 'microposts',
            },
        ),
    ]

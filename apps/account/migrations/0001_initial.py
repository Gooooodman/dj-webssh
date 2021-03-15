# Generated by Django 3.0.7 on 2021-03-15 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('password_hash', models.CharField(max_length=100)),
                ('type', models.CharField(default='default', max_length=20)),
                ('is_supper', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('access_token', models.CharField(max_length=32)),
                ('token_expired', models.IntegerField(null=True)),
                ('last_login', models.CharField(max_length=20)),
                ('last_ip', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
                'ordering': ('-id',),
            },
        ),
    ]

# Generated by Django 3.0.3 on 2020-09-01 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('face_name', models.CharField(max_length=10)),
                ('face_number', models.CharField(max_length=13)),
                ('business_id', models.CharField(max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLoginType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('social_login_id', models.CharField(max_length=45, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('social_login_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.SocialLoginType')),
            ],
        ),
    ]

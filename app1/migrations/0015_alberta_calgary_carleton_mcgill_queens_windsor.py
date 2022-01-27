# Generated by Django 4.0 on 2022-01-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_dalhousie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alberta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('university', models.CharField(max_length=100)),
                ('cgpa', models.CharField(max_length=4)),
                ('ielts', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Calgary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('university', models.CharField(max_length=100)),
                ('cgpa', models.CharField(max_length=4)),
                ('ielts', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Carleton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('university', models.CharField(max_length=100)),
                ('cgpa', models.CharField(max_length=4)),
                ('ielts', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Mcgill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('university', models.CharField(max_length=100)),
                ('cgpa', models.CharField(max_length=4)),
                ('ielts', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Queens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('university', models.CharField(max_length=100)),
                ('cgpa', models.CharField(max_length=4)),
                ('ielts', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Windsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('university', models.CharField(max_length=100)),
                ('cgpa', models.CharField(max_length=4)),
                ('ielts', models.CharField(max_length=4)),
            ],
        ),
    ]

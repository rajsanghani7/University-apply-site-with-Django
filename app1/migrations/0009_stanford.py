# Generated by Django 4.0 on 2022-01-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_princeton'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stanford',
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

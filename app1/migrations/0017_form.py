# Generated by Django 4.0.1 on 2022-01-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_delete_alberta_delete_boston_delete_calgary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('university', models.CharField(max_length=100)),
                ('cgpa', models.CharField(max_length=4)),
                ('ielts', models.CharField(max_length=4)),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-12-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='images')),
                ('price', models.CharField(max_length=255)),
                ('offer', models.BooleanField(default=False)),
                ('desc', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('city' , models.CharField(max_length=255)), 
                ('state',models.CharField(max_length=255)),  
                ('user_id',models.CharField(max_length=255)),
                ('is_vendor',models.CharField(max_length=255))
            ],
        ),
    ]

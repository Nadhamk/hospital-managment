# Generated by Django 4.2.10 on 2024-02-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_post_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='')),
                ('address', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]

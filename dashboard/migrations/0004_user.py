# Generated by Django 5.0.3 on 2024-03-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
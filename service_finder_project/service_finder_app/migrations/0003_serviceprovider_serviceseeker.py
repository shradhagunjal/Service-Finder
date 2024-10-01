# Generated by Django 5.1.1 on 2024-09-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_finder_app', '0002_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('seeker', 'Service Seeker'), ('provider', 'Service Provider')], max_length=10)),
                ('service_type', models.CharField(choices=[('plumbing', 'Plumbing'), ('teaching', 'Teaching'), ('cleaning', 'Cleaning'), ('electrician', 'Electrician')], max_length=20)),
                ('business_name', models.CharField(max_length=255)),
                ('service_description', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('home_address', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=15)),
                ('working_hours', models.CharField(max_length=50)),
                ('shop_image', models.ImageField(upload_to='shop_images/')),
                ('website', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('seeker', 'Service Seeker'), ('provider', 'Service Provider')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
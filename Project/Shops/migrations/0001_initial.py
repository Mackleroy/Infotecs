# Generated by Django 4.0.4 on 2022-05-20 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streets', to='Shops.city')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('house', models.CharField(max_length=255)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='Shops.city')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='Shops.street')),
            ],
        ),
    ]

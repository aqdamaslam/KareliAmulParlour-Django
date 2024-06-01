# Generated by Django 2.2.5 on 2019-09-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kap', '0002_amul_1_ltr_ice_cream_tubs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amul_2_Ltr_Ice_Cream_Bricks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.FileField(blank=True, upload_to='')),
                ('desc', models.TextField(blank=True, max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
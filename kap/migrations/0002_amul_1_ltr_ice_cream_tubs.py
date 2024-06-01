# Generated by Django 2.2.5 on 2019-09-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amul_1_Ltr_Ice_Cream_Tubs',
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
# Generated by Django 5.1.1 on 2024-09-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_brand_brandadmin_alter_car_brand'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BrandAdmin',
        ),
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

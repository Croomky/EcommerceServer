# Generated by Django 2.2 on 2019-04-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(upload_to='D:\\Projects\\EcommerceSolution\\EcommerceServer\\ecommerceserver\\static\\thumbnails'),
        ),
    ]

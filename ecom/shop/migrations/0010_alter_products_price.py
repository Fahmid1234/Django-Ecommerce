# Generated by Django 5.0.2 on 2024-06-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_products_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(),
        ),
    ]

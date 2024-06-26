# Generated by Django 5.0.6 on 2024-06-25 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('MEN', 'Men'), ('WOMEN', 'Women')], help_text='Choose the category type: Men or Women', max_length=10, unique=True)),
                ('slug', models.SlugField(help_text='Unique URL path segment for this category', max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category_product',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('views', models.PositiveIntegerField(default=0)),
                ('rating', models.PositiveSmallIntegerField(default=0, help_text='Rating from 0 to 5')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category')),
            ],
            options={
                'db_table': 'product',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['id', 'slug'], name='product_id_1d04b7_idx'), models.Index(fields=['name'], name='product_name_c4c985_idx'), models.Index(fields=['-created'], name='product_created_01e61b_idx')],
            },
        ),
    ]

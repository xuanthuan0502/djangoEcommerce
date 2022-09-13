# Generated by Django 3.1.7 on 2022-05-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20220520_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('mobilephone', 'mobilephone'), ('book', 'book'), ('laptop', 'laptop')], max_length=200, null=True),
        ),
    ]

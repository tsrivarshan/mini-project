# Generated by Django 3.2.3 on 2022-08-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_cart_cartentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='entries',
            field=models.ManyToManyField(blank=True, related_name='cart', to='store.CartEntry'),
        ),
    ]
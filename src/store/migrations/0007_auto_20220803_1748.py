# Generated by Django 3.2.3 on 2022-08-03 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0006_alter_cart_entries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='entries',
            field=models.ManyToManyField(blank=True, to='store.CartEntry'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 4.2.5 on 2023-09-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auction_image_alter_user_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='opening_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
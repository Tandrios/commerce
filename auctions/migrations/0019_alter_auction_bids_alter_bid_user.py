# Generated by Django 4.2.5 on 2023-09-19 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_rename_allbids_auction_bids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='bids',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.bid'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allbids', to=settings.AUTH_USER_MODEL),
        ),
    ]
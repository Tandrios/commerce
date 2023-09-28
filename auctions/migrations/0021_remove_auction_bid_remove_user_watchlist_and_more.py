# Generated by Django 4.2.5 on 2023-09-20 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_rename_bids_auction_bid_alter_bid_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='watchlist',
        ),
        migrations.AddField(
            model_name='auction',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='current_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='auction',
            name='opening_bid',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AddField(
            model_name='bid',
            name='auction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.auction'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('ET', 'Entertainment'), ('GV', 'Gebruiksvoorwerpen'), ('IT', ' IT'), ('AU', "Auto's"), ('DI', 'Divers')], default='DI', max_length=2),
        ),
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
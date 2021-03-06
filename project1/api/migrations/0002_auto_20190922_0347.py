# Generated by Django 2.2.2 on 2019-09-22 03:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliomodel',
            name='cash',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasemodel',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasemodel',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasemodel',
            name='symbol',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasemodel',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasemodel',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.UserModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='portfolio',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.PortfolioModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='symbol',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='api_token',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='password',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='portfolio',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.PortfolioModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='username',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]

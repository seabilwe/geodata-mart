# Generated by Django 3.2.13 on 2022-07-29 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(blank=True, default='Primary', max_length=255, null=True, verbose_name='Account Name')),
                ('account_balance', models.FloatField(default=0, verbose_name='Balance')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('is_organizational', models.BooleanField(blank=True, default=False, max_length=255, null=True, verbose_name='Organizational Account')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata', models.JSONField(verbose_name='Transaction Metadata')),
                ('value', models.FloatField(default=0, verbose_name='Transaction Value')),
                ('state', models.IntegerField(choices=[(0, 'Unspecified'), (1, 'Processed'), (2, 'Pending'), (3, 'Unprocessed'), (4, 'Reversed'), (5, 'Cancelled'), (6, 'Archived'), (7, 'Removed'), (8, 'Error'), (9, 'Other')], default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='credits.account')),
            ],
        ),
    ]

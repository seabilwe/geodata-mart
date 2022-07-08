# Generated by Django 3.2.13 on 2022-07-08 23:02

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='tasks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=36), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True, verbose_name='Job ID'),
        ),
        migrations.AlterField(
            model_name='job',
            name='parameters',
            field=models.JSONField(blank=True, null=True, verbose_name='Request Parameters'),
        ),
        migrations.AlterField(
            model_name='job',
            name='state',
            field=models.IntegerField(blank=True, choices=[(0, 'Unspecified'), (1, 'Abandoned'), (2, 'Unfulfilled'), (3, 'Processed'), (4, 'Completed'), (5, 'Failed'), (6, 'Processing'), (7, 'Unknown'), (8, 'Stale'), (9, 'Other')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='short_name',
            field=models.CharField(max_length=80, verbose_name='Layer Short Name'),
        ),
        migrations.AlterField(
            model_name='resultfile',
            name='job_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maps.job', verbose_name='Job'),
        ),
        migrations.AlterUniqueTogether(
            name='layer',
            unique_together={('short_name', 'project_id')},
        ),
    ]

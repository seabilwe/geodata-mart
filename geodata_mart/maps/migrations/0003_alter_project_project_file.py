# Generated by Django 3.2.13 on 2022-07-10 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20220708_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maps.qgisprojectfile', verbose_name='Project File'),
        ),
    ]

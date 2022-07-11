# Generated by Django 3.2.13 on 2022-07-11 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_alter_vendor_name'),
        ('maps', '0003_alter_project_project_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='config_auth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maps.authdbfile', verbose_name='QGIS Auth DB'),
        ),
        migrations.AlterField(
            model_name='project',
            name='config_pgservice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maps.pgservicefile', verbose_name='PG Service File'),
        ),
        migrations.AlterField(
            model_name='project',
            name='config_qgis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maps.qgisinifile', verbose_name='QGIS Configuration File'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maps.qgisprojectfile', verbose_name='Project File'),
        ),
        migrations.AlterField(
            model_name='project',
            name='vendor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vendors.vendor', verbose_name='Data Vendor'),
        ),
    ]

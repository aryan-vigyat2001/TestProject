# Generated by Django 3.2.5 on 2021-07-23 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_poj_stockid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poj',
            name='grosswt',
        ),
        migrations.RemoveField(
            model_name='poj',
            name='location',
        ),
        migrations.AddField(
            model_name='poj',
            name='olocation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.loc'),
        ),
        migrations.AddField(
            model_name='poj',
            name='phone_number',
            field=models.BigIntegerField(blank=True, default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poj',
            name='center_stone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.centerstone'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='cert',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.certificate'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='color_of_center_stone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.colorofcstone'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='jewellery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.jewell'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='metal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.metal1'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='shape',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.shape1'),
        ),
    ]
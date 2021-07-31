# Generated by Django 3.2.5 on 2021-07-28 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0022_alter_poj_cert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poj',
            name='color_of_center_stone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.colorofcstone'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='jewellery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.jewell'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.loc'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='metal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.metal1'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='shape',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.shape1'),
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-23 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_countries_gemtype_purchased'),
    ]

    operations = [
        migrations.CreateModel(
            name='centerstone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='colorofcstone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curr', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='jewell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jewel', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='loc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='metal1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metal', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='shape1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='POJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grosswt', models.BigIntegerField()),
                ('center_stone', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.centerstone')),
                ('cert', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.certificate')),
                ('color_of_center_stone', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.colorofcstone')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.purchased')),
                ('jewellery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.jewell')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.loc')),
                ('metal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.metal1')),
                ('shape', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.shape1')),
            ],
        ),
    ]

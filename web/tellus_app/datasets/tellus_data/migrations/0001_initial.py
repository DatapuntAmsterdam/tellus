# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-09 13:51
from __future__ import unicode_literals

import compositefk.fields
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LengteCategorie',
            fields=[
                ('categorie', models.CharField(default='X', max_length=2, primary_key=True, serialize=False)),
                ('lengte_van', models.CharField(default='0', max_length=10)),
                ('lengte_tot', models.CharField(blank=True, default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Locatie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetlocatie', models.IntegerField()),
                ('telpunt', models.CharField(max_length=256)),
                ('straat', models.CharField(max_length=150)),
                ('windrichting', models.CharField(blank=True, max_length=20, null=True)),
                ('zijstraat1', models.CharField(blank=True, max_length=256, null=True)),
                ('zijstraat2', models.CharField(blank=True, max_length=256, null=True)),
                ('richting', models.CharField(max_length=256)),
                ('ingangsdatum', models.DateField(blank=True, null=True)),
                ('eindedatum', models.DateField(blank=True, null=True)),
                ('geometrie', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=28992)),
                ('lengtecategorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tellus_data.LengteCategorie')),
            ],
        ),
        migrations.CreateModel(
            name='SnelheidsCategorie',
            fields=[
                ('categorie', models.IntegerField(primary_key=True, serialize=False)),
                ('s1', models.CharField(default='nvt', max_length=30)),
                ('s2', models.CharField(default='nvt', max_length=30)),
                ('s3', models.CharField(default='nvt', max_length=30)),
                ('s4', models.CharField(default='nvt', max_length=30)),
                ('s5', models.CharField(default='nvt', max_length=30)),
                ('s6', models.CharField(default='nvt', max_length=30)),
                ('s7', models.CharField(default='nvt', max_length=30)),
                ('s8', models.CharField(default='nvt', max_length=30)),
                ('s9', models.CharField(default='nvt', max_length=30)),
                ('s10', models.CharField(default='nvt', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Telling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetlocatie', models.IntegerField()),
                ('richting', models.IntegerField(blank=True, null=True)),
                ('validatie', models.IntegerField()),
                ('representatief', models.IntegerField()),
                ('meetraai', models.IntegerField()),
                ('classificatie', models.IntegerField()),
                ('tijd_van', models.DateTimeField(auto_now_add=True)),
                ('tijd_tot', models.DateTimeField(auto_now_add=True)),
                ('c1', models.IntegerField(null=True)),
                ('c2', models.IntegerField(null=True)),
                ('c3', models.IntegerField(null=True)),
                ('c4', models.IntegerField(null=True)),
                ('c5', models.IntegerField(null=True)),
                ('c6', models.IntegerField(null=True)),
                ('c7', models.IntegerField(null=True)),
                ('c8', models.IntegerField(null=True)),
                ('c9', models.IntegerField(null=True)),
                ('c10', models.IntegerField(null=True)),
                ('c11', models.IntegerField(null=True)),
                ('c12', models.IntegerField(null=True)),
                ('c13', models.IntegerField(null=True)),
                ('c14', models.IntegerField(null=True)),
                ('c15', models.IntegerField(null=True)),
                ('c16', models.IntegerField(null=True)),
                ('c17', models.IntegerField(null=True)),
                ('c18', models.IntegerField(null=True)),
                ('c19', models.IntegerField(null=True)),
                ('c20', models.IntegerField(null=True)),
                ('c21', models.IntegerField(null=True)),
                ('c22', models.IntegerField(null=True)),
                ('c23', models.IntegerField(null=True)),
                ('c24', models.IntegerField(null=True)),
                ('c25', models.IntegerField(null=True)),
                ('c26', models.IntegerField(null=True)),
                ('c27', models.IntegerField(null=True)),
                ('c28', models.IntegerField(null=True)),
                ('c29', models.IntegerField(null=True)),
                ('c30', models.IntegerField(null=True)),
                ('c31', models.IntegerField(null=True)),
                ('c32', models.IntegerField(null=True)),
                ('c33', models.IntegerField(null=True)),
                ('c34', models.IntegerField(null=True)),
                ('c35', models.IntegerField(null=True)),
                ('c36', models.IntegerField(null=True)),
                ('c37', models.IntegerField(null=True)),
                ('c38', models.IntegerField(null=True)),
                ('c39', models.IntegerField(null=True)),
                ('c40', models.IntegerField(null=True)),
                ('c41', models.IntegerField(null=True)),
                ('c42', models.IntegerField(null=True)),
                ('c43', models.IntegerField(null=True)),
                ('c44', models.IntegerField(null=True)),
                ('c45', models.IntegerField(null=True)),
                ('c46', models.IntegerField(null=True)),
                ('c47', models.IntegerField(null=True)),
                ('c48', models.IntegerField(null=True)),
                ('c49', models.IntegerField(null=True)),
                ('c50', models.IntegerField(null=True)),
                ('c51', models.IntegerField(null=True)),
                ('c52', models.IntegerField(null=True)),
                ('c53', models.IntegerField(null=True)),
                ('c54', models.IntegerField(null=True)),
                ('c55', models.IntegerField(null=True)),
                ('c56', models.IntegerField(null=True)),
                ('c57', models.IntegerField(null=True)),
                ('c58', models.IntegerField(null=True)),
                ('c59', models.IntegerField(null=True)),
                ('c60', models.IntegerField(null=True)),
                ('locatie', compositefk.fields.CompositeForeignKey(default=0, null_if_equal=[], on_delete=django.db.models.deletion.CASCADE, related_name='locaties', to='tellus_data.Locatie', to_fields={'meetlocatie': compositefk.fields.LocalFieldValue('meetlocatie'), 'richting': compositefk.fields.LocalFieldValue('richting')})),
            ],
        ),
        migrations.AddField(
            model_name='locatie',
            name='snelheidscategorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tellus_data.SnelheidsCategorie'),
        ),
        migrations.AlterUniqueTogether(
            name='locatie',
            unique_together=set([('meetlocatie', 'richting')]),
        ),
    ]

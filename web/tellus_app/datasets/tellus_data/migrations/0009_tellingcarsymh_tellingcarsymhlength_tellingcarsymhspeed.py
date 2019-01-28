# Generated by Django 2.1.5 on 2019-01-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tellus_data', '0008_materialized_view_tellingen_Y_M_H_dag_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TellingCarsYMH',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('richting', models.IntegerField()),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('hour', models.IntegerField()),
                ('dag_type', models.CharField(choices=[('Weekend', 'Weekend'), ('Werkdag', 'Werkdag')], max_length=80)),
                ('aantal', models.IntegerField()),
                ('aantal_dagen', models.IntegerField()),
            ],
            options={
                'db_table': 'tellus_data_year_month_hour',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TellingCarsYMHLength',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('richting', models.IntegerField()),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('hour', models.IntegerField()),
                ('dag_type', models.CharField(choices=[('Weekend', 'Weekend'), ('Werkdag', 'Werkdag')], max_length=80)),
                ('aantal', models.IntegerField()),
                ('aantal_dagen', models.IntegerField()),
                ('lengte_label', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'tellus_data_year_month_hour_length',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TellingCarsYMHSpeed',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('richting', models.IntegerField()),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('hour', models.IntegerField()),
                ('dag_type', models.CharField(choices=[('Weekend', 'Weekend'), ('Werkdag', 'Werkdag')], max_length=80)),
                ('aantal', models.IntegerField()),
                ('aantal_dagen', models.IntegerField()),
                ('snelheids_label', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'tellus_data_year_month_hour_speed',
                'managed': False,
            },
        ),
    ]

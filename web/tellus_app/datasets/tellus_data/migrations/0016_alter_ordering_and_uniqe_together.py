# Generated by Django 2.1.1 on 2018-09-10 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tellus_data', '0015_expanded_view_add_location_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tellusdata',
            options={'ordering': ['id', 'tijd_van', 'tijd_tot', 'richting']},
        ),
        migrations.AlterUniqueTogether(
            name='tellusdata',
            unique_together={('tellus', 'richting', 'tijd_van', 'tijd_tot')},
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-25 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamstudent', '0006_auto_20200325_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ausbildung_typ_arzt_sonstige',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='ausbildung_typ_sonstige_eintragen',
            field=models.CharField(blank=True, default=False, max_length=200),
        ),
    ]

# Generated by Django 3.0.4 on 2020-04-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamstudent', '0012_merge_20200406_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtosend',
            name='send_date',
            field=models.DateTimeField(null=True),
        ),
    ]

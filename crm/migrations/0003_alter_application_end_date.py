# Generated by Django 3.2.5 on 2021-07-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_application_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='end_date',
            field=models.DateField(help_text='Deadline'),
        ),
    ]

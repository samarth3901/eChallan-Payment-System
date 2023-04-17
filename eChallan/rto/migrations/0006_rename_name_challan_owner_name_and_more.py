# Generated by Django 4.1.5 on 2023-03-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rto', '0005_alter_challan_offender_email_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challan',
            old_name='name',
            new_name='owner_name',
        ),
        migrations.RenameField(
            model_name='challan',
            old_name='sections',
            new_name='rule_id',
        ),
        migrations.RemoveField(
            model_name='challan',
            name='license_no',
        ),
        migrations.AddField(
            model_name='challan',
            name='suspect_name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]

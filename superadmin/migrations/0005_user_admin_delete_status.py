# Generated by Django 5.1.6 on 2025-05-30 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0004_rename_user_user_admin_alter_user_admin_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_admin',
            name='delete_status',
            field=models.CharField(max_length=25, null=True),
        ),
    ]

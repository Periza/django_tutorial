# Generated by Django 4.1.6 on 2023-02-16 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='date_adde',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='topis',
            new_name='topic',
        ),
    ]

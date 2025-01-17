# Generated by Django 5.0.4 on 2024-07-31 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidtasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_completed',
            new_name='completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='completion_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='consecutive_days',
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateField(),
        ),
    ]

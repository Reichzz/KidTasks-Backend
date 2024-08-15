# Generated by Django 5.0.6 on 2024-08-10 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidtasks', '0004_alter_task_creation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('streak', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='creation_date',
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='child',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='kidtasks.child'),
            preserve_default=False,
        ),
    ]
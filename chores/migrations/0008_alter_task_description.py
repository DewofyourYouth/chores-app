# Generated by Django 4.0.5 on 2022-06-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0007_alter_task_chore_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0006_alter_task_points_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='chore_type',
            field=models.IntegerField(choices=[(1, 'Daily'), (2, 'Alternating'), (3, 'Extra Credit')]),
        ),
    ]

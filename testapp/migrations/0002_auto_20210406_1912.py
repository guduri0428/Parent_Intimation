# Generated by Django 3.1.8 on 2021-04-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student_attendance',
        ),
        migrations.RemoveField(
            model_name='admintable',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student_marks',
            name='id',
        ),
        migrations.AlterField(
            model_name='admintable',
            name='admin_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student_marks',
            name='parent_phone',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='student_marks',
            name='student_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]

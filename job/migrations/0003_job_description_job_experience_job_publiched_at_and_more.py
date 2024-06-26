# Generated by Django 4.2.6 on 2023-10-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='job',
            name='publiched_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]

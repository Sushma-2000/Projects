# Generated by Django 3.2.7 on 2021-09-07 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_user_taken_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='oops_userans',
            name='num',
            field=models.IntegerField(default=1),
        ),
    ]
# Generated by Django 3.2 on 2021-04-19 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boilerplate', '0004_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='thought',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 3.2 on 2021-04-18 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boilerplate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='conversation',
            new_name='conversation_id',
        ),
        migrations.RenameField(
            model_name='thought',
            old_name='message',
            new_name='message_id',
        ),
    ]

# Generated by Django 4.1 on 2022-11-26 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='answers_en',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='answers_ru',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='questions_en',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='questions_ru',
        ),
        migrations.RemoveField(
            model_name='sendmessage',
            name='message_en',
        ),
        migrations.RemoveField(
            model_name='sendmessage',
            name='message_ru',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='position_en',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='position_ru',
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-24 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_user_wallet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_wallet',
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_adminuser_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminuser',
            name='full_names',
            field=models.CharField(default='Zilo', max_length=60),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-06 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]

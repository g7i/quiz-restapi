# Generated by Django 3.0.1 on 2019-12-31 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default='hello', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='doc',
            field=models.FileField(upload_to='notes/'),
        ),
    ]
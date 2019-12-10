# Generated by Django 2.2.7 on 2019-12-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_a',
            new_name='a',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='choice_b',
            new_name='b',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='choice_c',
            new_name='c',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='choice_d',
            new_name='d',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='choice',
            name='answer',
            field=models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')], default='a', max_length=1),
            preserve_default=False,
        ),
    ]
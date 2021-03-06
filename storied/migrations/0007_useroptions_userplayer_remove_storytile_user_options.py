# Generated by Django 4.0.4 on 2022-06-02 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storied', '0006_story_play_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_options', models.CharField(blank=True, choices=[('FW', 'Forward'), ('BW', 'Backward'), ('LF', 'Left'), ('RT', 'Right'), ('AT', 'Attack'), ('PU', 'Pick-up')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=40)),
                ('health_points', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='storytile',
            name='user_options',
        ),
    ]

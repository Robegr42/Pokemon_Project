# Generated by Django 3.2.3 on 2021-05-31 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_world', '0002_auto_20210530_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='personalkey',
        ),
        migrations.AddField(
            model_name='trainer',
            name='username',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
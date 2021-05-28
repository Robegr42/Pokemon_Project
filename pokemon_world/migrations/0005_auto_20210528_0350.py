# Generated by Django 3.2.3 on 2021-05-28 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_world', '0004_alter_movement_element'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='element', to='pokemon_world.element'),
        ),
        migrations.AlterField(
            model_name='specie',
            name='movements',
            field=models.ManyToManyField(blank=True, to='pokemon_world.Movement'),
        ),
    ]

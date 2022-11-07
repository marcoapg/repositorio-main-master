# Generated by Django 4.1.1 on 2022-10-07 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCompeticion', '0002_initial'),
        ('appPartido', '0003_formacion_remove_encuentro_equipo_local_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sede',
            name='estado_id',
        ),
        migrations.RemoveField(
            model_name='sede',
            name='pais_id',
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais_id',
            field=models.ForeignKey(db_column='pais_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.pais'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sede',
            name='estado',
            field=models.CharField(default='DI', max_length=2),
        ),
    ]

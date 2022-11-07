# Generated by Django 4.1.1 on 2022-10-07 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appEquipo', '0002_initial'),
        ('appPartido', '0002_alter_sede_fecha_inauguracion'),
    ]

    operations = [
        migrations.CreateModel(
            name='formacion',
            fields=[
                ('formacion_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'formacion',
            },
        ),
        migrations.RemoveField(
            model_name='encuentro',
            name='equipo_local_id',
        ),
        migrations.RemoveField(
            model_name='encuentro',
            name='equipo_visitante_id',
        ),
        migrations.RemoveField(
            model_name='encuentro',
            name='resultado_equipo_a',
        ),
        migrations.RemoveField(
            model_name='encuentro',
            name='resultado_equipo_b',
        ),
        migrations.RemoveField(
            model_name='encuentro',
            name='resultado_general',
        ),
        migrations.AddField(
            model_name='evento_persona',
            name='observacion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='evento_persona',
            name='suceso',
            field=models.CharField(default='ABC', max_length=5),
        ),
        migrations.AddField(
            model_name='evento_persona',
            name='tipo_suceso',
            field=models.CharField(blank=True, choices=[('E', 'ENTRADA'), ('S', 'SALIDA')], max_length=1, null=True),
        ),
        migrations.CreateModel(
            name='detalle_encuentro',
            fields=[
                ('detalle_encuentro_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo_equipo', models.CharField(choices=[('L', 'LOCAL'), ('V', 'VISITA')], max_length=1)),
                ('resultado', models.CharField(max_length=3)),
                ('encuentro_id', models.ForeignKey(db_column='encuentro_id', on_delete=django.db.models.deletion.CASCADE, to='appPartido.encuentro')),
                ('equipo_id', models.ForeignKey(db_column='equipo_id', on_delete=django.db.models.deletion.CASCADE, to='appEquipo.equipo')),
                ('formacion_id', models.ForeignKey(db_column='formacion_id', on_delete=django.db.models.deletion.CASCADE, to='appPartido.formacion')),
            ],
            options={
                'verbose_name_plural': 'detalle_encuentro',
            },
        ),
    ]
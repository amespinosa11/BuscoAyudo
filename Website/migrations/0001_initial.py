# Generated by Django 2.1 on 2018-10-08 01:29
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=1000)),
                ('correo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TiposDeServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(upload_to='services')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('apellidos', models.CharField(max_length=1000)),
                ('aniosExperiencia', models.IntegerField()),
                ('telefono', models.CharField(max_length=1000)),
                ('correo', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(upload_to='photos')),
                ('tiposDeServicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Website.TiposDeServicio')),
                ('usuarioId', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='trabajador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Website.Trabajador'),
        ),
    ]

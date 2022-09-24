# Generated by Django 4.1.1 on 2022-09-24 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_agenda', '0007_posteo_plantas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posteo_interacciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=60)),
                ('pais', models.CharField(max_length=40)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes')),
                ('fecha', models.DateField()),
                ('autor', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Planta',
        ),
    ]
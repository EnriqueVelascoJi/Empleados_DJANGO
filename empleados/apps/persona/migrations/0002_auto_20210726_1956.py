# Generated by Django 3.2.5 on 2021-07-27 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='habilidades',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]

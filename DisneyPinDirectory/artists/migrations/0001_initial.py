# Generated by Django 4.0 on 2023-04-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('tags', models.ManyToManyField(blank=True, to='tags.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('serial_number', models.PositiveIntegerField()),
                ('pinterest_url', models.URLField(max_length=128)),
                ('links', models.TextField()),
                ('boards', models.ManyToManyField(blank=True, to='artists.Board')),
            ],
        ),
    ]

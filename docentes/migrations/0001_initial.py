# Generated by Django 2.2.6 on 2019-10-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('dataCad', models.DateTimeField(auto_now=True)),
                ('dataMod', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

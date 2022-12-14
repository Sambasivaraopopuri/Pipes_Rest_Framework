# Generated by Django 4.1 on 2022-08-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tilte', models.CharField(max_length=200)),
                ('Desc', models.CharField(max_length=1000)),
                ('Size', models.CharField(max_length=5)),
                ('Posted_By', models.CharField(max_length=150)),
                ('Qulity', models.CharField(max_length=25)),
                ('Grade', models.CharField(max_length=25)),
                ('Color', models.CharField(max_length=20)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'Pipes',
            },
        ),
    ]

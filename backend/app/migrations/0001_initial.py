# Generated by Django 5.0.2 on 2024-02-24 20:05

import app.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Your File', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(default='#000000', max_length=7, validators=[app.validators.validate_html5_color])),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('controlid', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(choices=[('Vocalizations', 'Vocalizations'), ('Right Lung Sound', 'Right Lung Sound'), ('Left Lung Sound', 'Left Lung Sound'), ('Left Femoral Pulse', 'Left Femoral Pulse'), ('Right Femoral Pulse', 'Right Femoral Pulse'), ('Left Dorsal Pulse', 'Left Dorsal Pulse'), ('Right Dorsal Pulse', 'Right Dorsal Pulse'), ('Heart Sounds', 'Heart Sounds'), ('Chest Movement', 'Chest Movement'), ('CPR', 'CPR'), ('ECG', 'ECG'), ('SpO2', 'SpO2'), ('ETCO2', 'ETCO2'), ('Cuff', 'Cuff'), ('Palpate', 'Palpate'), ('Temp', 'Temp')], default=('Vocalizations', 'Vocalizations'), max_length=256)),
                ('id', models.CharField(choices=[('vocals-dog-control', 'Vocalizations'), ('right-lung-dog-control', 'Right Lung Sound'), ('left-lung-dog-control', 'Left Lung Sound'), ('left-femoral-pulse-dog-control', 'Left Femoral Pulse'), ('right-femoral-pulse-dog-control', 'Right Femoral Pulse'), ('left-dorsal-pulse-dog-control', 'Left Dorsal Pulse'), ('right-dorsal-pulse-dog-control', 'Right Dorsal Pulse'), ('heart-sound-dog-control', 'Heart Sounds'), ('chest-dog-control', 'Chest Movement'), ('button-cpr', 'CPR'), ('button-ekg', 'ECG'), ('button-SpO2', 'SpO2'), ('button-CO2', 'ETCO2'), ('button-cuff', 'Cuff'), ('button-palpate', 'Palpate'), ('button-Tperi', 'Temp')], default=('vocals-dog-control', 'Vocalizations'), max_length=256)),
                ('top', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('left', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='controls', to='app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default='images/linus.jpg', max_length=256)),
                ('height_pct', models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('width_pct', models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='scenario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.scenario'),
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default='media/logo.jpeg', max_length=256)),
                ('title', models.CharField(default='Logo', max_length=256)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='app.scenario')),
            ],
        ),
        migrations.CreateModel(
            name='Init',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_scene', models.IntegerField()),
                ('record', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.scenario')),
            ],
        ),
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.FileField(default='images/linus.jpg', upload_to='images')),
                ('title', models.CharField(default='Linus', max_length=256)),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.scenario')),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='ovsscenariomgr', max_length=256)),
                ('date_of_creation', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField(default='OVS Scenario Manager')),
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.scenario')),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='Summary Description')),
                ('breed', models.CharField(default='Dalmation', max_length=64)),
                ('gender', models.CharField(default='Male', max_length=64)),
                ('weight', models.CharField(default='30 kg', max_length=6)),
                ('species', models.CharField(default='Canine', max_length=64)),
                ('symptoms', models.TextField(default='Summary Symptoms')),
                ('image', models.CharField(default='images/linus.jpg', max_length=256)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Titular Title', max_length=256)),
                ('top', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('left', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('header', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.header')),
            ],
        ),
        migrations.CreateModel(
            name='VocalFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default='vocals/purr.wav', max_length=256)),
                ('title', models.CharField(default='Purr', max_length=256)),
                ('vocals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vocals', to='app.scenario')),
            ],
        ),
    ]

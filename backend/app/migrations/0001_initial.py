# Generated by Django 5.0.2 on 2024-02-26 05:18

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
            name='Cardiac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rhythm', models.CharField(choices=[('sinus', 'Sinus rhythm'), ('afib', 'Atrial fibrillation'), ('vfib', 'Ventricular fibrillation'), ('vtach1', 'Ventricular tachycardia 1'), ('vtach2', 'Ventricular tachycardia 2'), ('ront', 'R-on-T'), ('asystole', 'Asystole')], default=('sinus', 'Sinus rhythm'), max_length=8)),
                ('vpc', models.CharField(choices=[('none', 'None'), ('1-1', 'vtach1-singlet'), ('1-2', 'vtach1-couplet'), ('1-3', 'vtach1-triplet'), ('2-1', 'vtach2-singlet'), ('2-2', 'vtach2-couplet'), ('2-3', 'vtach2-triplet'), ('3-1', 'vtach3-singlet'), ('3-2', 'vtach3-couplet'), ('3-3', 'vtach3-triplet')], default=('none', 'None'), max_length=4)),
                ('pea', models.IntegerField(choices=[(0, 'off'), (1, 'on')], default=0)),
                ('vpc_freq', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('vfib_amplitude', models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], default=('low', 'low'), max_length=6)),
                ('rate', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('nibp_rate', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('bps_sys', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('bps_dia', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(290)])),
                ('left_dorsal_pulse_strength', models.CharField(choices=[('none', 'none'), ('weak', 'weak'), ('medium', 'medium'), ('strong', 'strong')], default=('none', 'none'), max_length=6)),
                ('left_femoral_pulse_strength', models.CharField(choices=[('none', 'none'), ('weak', 'weak'), ('medium', 'medium'), ('strong', 'strong')], default=('none', 'none'), max_length=6)),
                ('right_dorsal_pulse_strength', models.CharField(choices=[('none', 'none'), ('weak', 'weak'), ('medium', 'medium'), ('strong', 'strong')], default=('none', 'none'), max_length=6)),
                ('heart_sound_volume', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('heart_sound', models.CharField(choices=[('normal', 'Normal'), ('systolic_murmur', 'Systolic Murmur'), ('pansystolic_murmur', 'Pansystolic Murmur'), ('holosystolic_murmur', 'Holosystolic Murmur'), ('continuous_murmur', 'Continuous Murmur'), ('diastolic_murmur', 'Diastolic Murmur'), ('gallop', 'Gallop')], default=('normal', 'Normal'), max_length=20)),
                ('ecg_indicator', models.IntegerField(choices=[(0, 'not illuminated'), (1, 'illuminated')], default=(0, 'not illuminated'))),
                ('bp_cuff', models.IntegerField(choices=[(0, 'not illuminated'), (1, 'illuminated')], default=(0, 'not illuminated'))),
                ('arrest', models.IntegerField(choices=[(0, 'not illuminated'), (1, 'illuminated')], default=(0, 'not illuminated'))),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Your File', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField(default=975, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1100)])),
                ('temperature_enable', models.IntegerField(choices=[(0, 'off'), (1, 'on')], default=0)),
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
            name='Respiration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_lung_sound', models.CharField(choices=[('normal', 'Normal'), ('coarse_crackles', 'Course crackles'), ('fine_crackels', 'Fine crackles'), ('wheezes', 'Wheezes'), ('stridor', 'Stridor'), ('stertor', 'Stertor'), ('same_as_right', 'Same as right')], default=('normal', 'Normal'), max_length=16)),
                ('left_lung_sound_volume', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('right_lung_sound', models.CharField(choices=[('normal', 'Normal'), ('coarse_crackles', 'Course crackles'), ('fine_crackels', 'Fine crackles'), ('wheezes', 'Wheezes'), ('stridor', 'Stridor'), ('stertor', 'Stertor'), ('same_as_left', 'Same as left')], default=('normal', 'Normal'), max_length=16)),
                ('right_lung_sound_volume', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('inhalation_duration', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('exhalation_duration', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('spo2', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('etco2', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)])),
                ('rate', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)])),
                ('spo2_indicator', models.IntegerField(choices=[(0, 'Not connected'), (1, 'connected')], default=0)),
                ('etco2_indicator', models.IntegerField(choices=[(0, 'Not connected'), (1, 'connected')], default=0)),
                ('chest_movement', models.IntegerField(choices=[(0, 'off'), (1, 'on')], default=0)),
                ('manual_count', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
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
                ('initial_scene', models.IntegerField(default=1)),
                ('record', models.IntegerField(default=1)),
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.scenario')),
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

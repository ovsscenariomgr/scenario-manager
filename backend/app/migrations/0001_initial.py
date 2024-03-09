# Generated by Django 4.2.10 on 2024-03-09 21:14

import app.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cardiac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rhythm', models.CharField(choices=[('sinus', 'Sinus rhythm'), ('afib', 'Atrial fibrillation'), ('vfib', 'Ventricular fibrillation'), ('vtach1', 'Ventricular tachycardia 1'), ('vtach2', 'Ventricular tachycardia 2'), ('ront', 'R-on-T'), ('asystole', 'Asystole')], default='sinus', max_length=8)),
                ('vpc', models.CharField(choices=[('none', 'None'), ('1-1', 'Vtach1 Singlet'), ('1-2', 'Vtach1 Couplet'), ('1-3', 'Vtach1 Triplet'), ('2-1', 'Vtach2 Singlet'), ('2-2', 'Vtach2 Couplet'), ('2-3', 'Vtach2 Triplet'), ('3-1', 'Vtach3 Singlet'), ('3-2', 'Vtach3 Couplet'), ('3-3', 'Vtach3 Triplet')], default='none', max_length=4)),
                ('pea', models.IntegerField(choices=[(0, 'Off'), (1, 'On')], default=0)),
                ('vpc_freq', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('vfib_amplitude', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=6)),
                ('rate', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('nibp_rate', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('bps_sys', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('bps_dia', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(290)])),
                ('left_dorsal_pulse_strength', models.CharField(choices=[('none', 'None'), ('weak', 'Weak'), ('medium', 'Medium'), ('strong', 'Strong')], default='none', max_length=6)),
                ('right_dorsal_pulse_strength', models.CharField(choices=[('none', 'None'), ('weak', 'Weak'), ('medium', 'Medium'), ('strong', 'Strong')], default='none', max_length=6)),
                ('left_femoral_pulse_strength', models.CharField(choices=[('none', 'None'), ('weak', 'Weak'), ('medium', 'Medium'), ('strong', 'Strong')], default='none', max_length=6)),
                ('right_femoral_pulse_strength', models.CharField(choices=[('none', 'None'), ('weak', 'Weak'), ('medium', 'Medium'), ('strong', 'Strong')], default='none', max_length=6)),
                ('heart_sound_volume', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('heart_sound', models.CharField(choices=[('normal', 'Normal'), ('systolic_murmur', 'Systolic Murmur'), ('pansystolic_murmur', 'Pansystolic Murmur'), ('holosystolic_murmur', 'Holosystolic Murmur'), ('continuous_murmur', 'Continuous Murmur'), ('diastolic_murmur', 'Diastolic Murmur'), ('gallop', 'Gallop')], default='normal', max_length=20)),
                ('ecg_indicator', models.IntegerField(choices=[(0, 'Not Illuminated'), (1, 'Illuminated')], default=0)),
                ('bp_cuff', models.IntegerField(choices=[(0, 'Not Illuminated'), (1, 'Illuminated')], default=0)),
                ('arrest', models.IntegerField(choices=[(0, 'Not Illuminated'), (1, 'Illuminated')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='drugs', max_length=64)),
                ('title', models.CharField(default='Injected Drugs', max_length=64)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
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
                ('temperature_enable', models.IntegerField(choices=[(0, 'Off'), (1, 'On')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='ovsscenariomgr', max_length=256)),
                ('date_of_creation', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField(default='OVS Scenario Manager')),
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
                ('left_lung_sound', models.CharField(choices=[('normal', 'Normal'), ('coarse_crackles', 'Coarse Crackles'), ('fine_crackles', 'Fine Crackles'), ('wheezes', 'Wheezes'), ('stridor', 'Stridor'), ('stertor', 'Stertor'), ('same_as_right', 'Same As Right'), ('same_as_left', 'Same As Left')], default='normal', max_length=16)),
                ('left_lung_sound_volume', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('right_lung_sound', models.CharField(choices=[('normal', 'Normal'), ('coarse_crackles', 'Coarse Crackles'), ('fine_crackles', 'Fine Crackles'), ('wheezes', 'Wheezes'), ('stridor', 'Stridor'), ('stertor', 'Stertor'), ('same_as_right', 'Same As Right'), ('same_as_left', 'Same As Left')], default='normal', max_length=16)),
                ('right_lung_sound_volume', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('inhalation_duration', models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(0)])),
                ('exhalation_duration', models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(0)])),
                ('spo2', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('spo2_indicator', models.IntegerField(choices=[(0, 'Not Connected'), (1, 'Connected')], default=0)),
                ('etco2', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)])),
                ('etco2_indicator', models.IntegerField(choices=[(0, 'Not Connected'), (1, 'Connected')], default=0)),
                ('rate', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)])),
                ('chest_movement', models.IntegerField(choices=[(0, 'Off'), (1, 'On')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('sceneid', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Opening Scene', max_length=256)),
                ('id', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('triggers_needed', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenes', to='app.scenario')),
            ],
        ),
        migrations.CreateModel(
            name='VocalFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default='vocals/purr.wav', max_length=256)),
                ('title', models.CharField(default='Purr', max_length=256)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vocals', to='app.scenario')),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.IntegerField(default=1)),
                ('scene_id', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('event_id', models.CharField(default='aed', max_length=64)),
                ('test', models.CharField(choices=[('eq', 'Eq'), ('gt', 'Gt'), ('lt', 'Lt'), ('lte', 'Lte'), ('gte', 'Gte'), ('inside', 'Inside'), ('outside', 'Outside'), ('', 'None')], default='eq', max_length=7)),
                ('cpr_duration', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('scenefk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='triggers', to='app.scene')),
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
            name='Timeout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeout_value', models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(0)])),
                ('scene_id', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('scenefk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.scene')),
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
            name='SceneInit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummy_field', models.IntegerField(default=1)),
                ('scene', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='init', to='app.scene')),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioInit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_scene', models.IntegerField(default=1)),
                ('record', models.IntegerField(default=1)),
                ('scenario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='init', to='app.scenario')),
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
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='app.scenario')),
            ],
        ),
        migrations.AddField(
            model_name='header',
            name='scenario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.scenario'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventid', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Morphine', max_length=256)),
                ('id', models.CharField(default='opiate_morphine', max_length=256)),
                ('priority', models.IntegerField(default=0)),
                ('hotkey', models.CharField(blank=True, default='', max_length=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('controlid', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='vocals-dog-control', max_length=256)),
                ('id', models.CharField(choices=[('vocals-dog-control', 'Vocalizations'), ('right-lung-dog-control', 'Right Lung Sound'), ('left-lung-dog-control', 'Left Lung Sound'), ('left-femoral-pulse-dog-control', 'Left Femoral Pulse'), ('right-femoral-pulse-dog-control', 'Right Femoral Pulse'), ('left-dorsal-pulse-dog-control', 'Left Dorsal Pulse'), ('right-dorsal-pulse-dog-control', 'Right Dorsal Pulse'), ('heart-sound-dog-control', 'Heart Sounds'), ('chest-dog-control', 'Chest Movement'), ('button-cpr', 'Cpr'), ('button-ekg', 'Ekg'), ('button-SpO2', 'Spo2'), ('button-CO2', 'Etco2'), ('button-cuff', 'Cuff'), ('button-palpate', 'Palpate'), ('button-Tperi', 'Temp')], default='vocals-dog-control', max_length=256)),
                ('top', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('left', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='controls', to='app.profile')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='app.scenario'),
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
        migrations.CreateModel(
            name='SceneInitRespiration',
            fields=[
                ('respiration_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.respiration')),
                ('scene_init', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='respiration', to='app.sceneinit')),
            ],
            bases=('app.respiration',),
        ),
        migrations.CreateModel(
            name='SceneInitGeneral',
            fields=[
                ('general_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.general')),
                ('scene_init', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='general', to='app.sceneinit')),
            ],
            bases=('app.general',),
        ),
        migrations.CreateModel(
            name='SceneInitCardiac',
            fields=[
                ('cardiac_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.cardiac')),
                ('scene_init', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cardiac', to='app.sceneinit')),
            ],
            bases=('app.cardiac',),
        ),
        migrations.CreateModel(
            name='ScenarioInitRespiration',
            fields=[
                ('respiration_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.respiration')),
                ('scenario_init', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='respiration', to='app.scenarioinit')),
            ],
            bases=('app.respiration',),
        ),
        migrations.CreateModel(
            name='ScenarioInitGeneral',
            fields=[
                ('general_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.general')),
                ('scenario_init', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='general', to='app.scenarioinit')),
            ],
            bases=('app.general',),
        ),
        migrations.CreateModel(
            name='ScenarioInitCardiac',
            fields=[
                ('cardiac_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.cardiac')),
                ('scenario_init', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cardiac', to='app.scenarioinit')),
            ],
            bases=('app.cardiac',),
        ),
        migrations.CreateModel(
            name='ParameterTriggerRespiration',
            fields=[
                ('respiration_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.respiration')),
                ('manual_count', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('trigger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='respiration', to='app.trigger')),
            ],
            bases=('app.respiration',),
        ),
        migrations.CreateModel(
            name='ParameterTriggerGeneral',
            fields=[
                ('general_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.general')),
                ('trigger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='general', to='app.trigger')),
            ],
            bases=('app.general',),
        ),
        migrations.CreateModel(
            name='ParameterTriggerCardiac',
            fields=[
                ('cardiac_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.cardiac')),
                ('trigger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cardiac', to='app.trigger')),
            ],
            bases=('app.cardiac',),
        ),
    ]

<template>
  <div>
    <div class="text-subtitle1 q-mt-sm">Cardiac</div>
    <div class="row q-col-gutter-sm">
      <div class="col-6 col-md-3">
        <q-select v-model="cardiac.rhythm" :options="rhythmOptions" emit-value map-options label="Rhythm" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-select v-model="cardiac.vpc" :options="vpcOptions" emit-value map-options label="VPC" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-select
          v-model="cardiac.vfib_amplitude"
          :options="vfibAmplitudeOptions"
          emit-value
          map-options
          label="VFib Amplitude"
          dense
        />
      </div>
      <div class="col-6 col-md-3">
        <q-select
          v-model="cardiac.heart_sound"
          :options="heartSoundOptions"
          emit-value
          map-options
          label="Heart Sound"
          dense
        />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="cardiac.rate" type="number" label="Rate" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="cardiac.nibp_rate" type="number" label="NIBP Rate" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="cardiac.bps_sys" type="number" label="BP Systolic" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="cardiac.bps_dia" type="number" label="BP Diastolic" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="cardiac.vpc_freq" type="number" label="VPC Frequency" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="cardiac.heart_sound_volume" type="number" label="Heart Sound Volume" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-select
          v-model="cardiac.left_dorsal_pulse_strength"
          :options="pulseStrengthOptions"
          emit-value
          map-options
          label="Left Dorsal Pulse"
          dense
        />
      </div>
      <div class="col-6 col-md-3">
        <q-select
          v-model="cardiac.right_dorsal_pulse_strength"
          :options="pulseStrengthOptions"
          emit-value
          map-options
          label="Right Dorsal Pulse"
          dense
        />
      </div>
      <div class="col-6 col-md-3">
        <q-select
          v-model="cardiac.left_femoral_pulse_strength"
          :options="pulseStrengthOptions"
          emit-value
          map-options
          label="Left Femoral Pulse"
          dense
        />
      </div>
      <div class="col-6 col-md-3">
        <q-select
          v-model="cardiac.right_femoral_pulse_strength"
          :options="pulseStrengthOptions"
          emit-value
          map-options
          label="Right Femoral Pulse"
          dense
        />
      </div>
      <div class="col-6 col-md-3">
        <q-toggle v-model="cardiac.pea" :true-value="1" :false-value="0" label="PEA" />
      </div>
      <div class="col-6 col-md-3">
        <q-toggle v-model="cardiac.ecg_indicator" :true-value="1" :false-value="0" label="ECG Indicator" />
      </div>
      <div class="col-6 col-md-3">
        <q-toggle v-model="cardiac.bp_cuff" :true-value="1" :false-value="0" label="BP Cuff Attached" />
      </div>
      <div class="col-6 col-md-3">
        <q-toggle v-model="cardiac.arrest" :true-value="1" :false-value="0" label="Arrest" />
      </div>
    </div>

    <div class="text-subtitle1 q-mt-md">Respiration</div>
    <div class="row q-col-gutter-sm">
      <div class="col-6 col-md-3">
        <q-select
          v-model="respiration.left_lung_sound"
          :options="lungSoundOptions"
          emit-value
          map-options
          label="Left Lung Sound"
          dense
        />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="respiration.left_lung_sound_volume" type="number" label="Left Lung Volume" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-select
          v-model="respiration.right_lung_sound"
          :options="lungSoundOptions"
          emit-value
          map-options
          label="Right Lung Sound"
          dense
        />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="respiration.right_lung_sound_volume" type="number" label="Right Lung Volume" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="respiration.rate" type="number" label="Rate" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="respiration.spo2" type="number" label="SpO2" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="respiration.etco2" type="number" label="EtCO2" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="respiration.inhalation_duration" type="number" label="Inhalation Duration" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-input v-model.number="respiration.exhalation_duration" type="number" label="Exhalation Duration" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-toggle v-model="respiration.spo2_indicator" :true-value="1" :false-value="0" label="SpO2 Connected" />
      </div>
      <div class="col-6 col-md-3">
        <q-toggle v-model="respiration.etco2_indicator" :true-value="1" :false-value="0" label="EtCO2 Connected" />
      </div>
      <div class="col-6 col-md-3">
        <q-toggle v-model="respiration.chest_movement" :true-value="1" :false-value="0" label="Chest Movement" />
      </div>
    </div>

    <div class="text-subtitle1 q-mt-md">General</div>
    <div class="row q-col-gutter-sm">
      <div class="col-6 col-md-3">
        <q-input v-model.number="general.temperature" type="number" label="Temperature" dense />
      </div>
      <div class="col-6 col-md-3">
        <q-toggle v-model="general.temperature_enable" :true-value="1" :false-value="0" label="Temperature Enabled" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { ScenarioInitCardiac, ScenarioInitRespiration, ScenarioInitGeneral } from 'src/types';
import { RhythmEnum, VpcEnum, VfibAmplitudeEnum, PulseStrengthEnum, HeartSoundEnum, LungSoundEnum } from 'src/types';

defineOptions({
  name: 'CardiacRespirationGeneralFields',
});

const cardiac = defineModel<ScenarioInitCardiac>('cardiac', { required: true });
const respiration = defineModel<ScenarioInitRespiration>('respiration', { required: true });
const general = defineModel<ScenarioInitGeneral>('general', { required: true });

function enumOptions(values: Record<string, string>) {
  return Object.values(values).map((value) => ({ label: value, value }));
}

const rhythmOptions = enumOptions(RhythmEnum);
const vpcOptions = enumOptions(VpcEnum);
const vfibAmplitudeOptions = enumOptions(VfibAmplitudeEnum);
const pulseStrengthOptions = enumOptions(PulseStrengthEnum);
const heartSoundOptions = enumOptions(HeartSoundEnum);
const lungSoundOptions = enumOptions(LungSoundEnum);
</script>

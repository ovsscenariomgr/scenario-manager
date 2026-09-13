import { defineStore, acceptHMRUpdate } from 'pinia';
import type { ScenarioInit, ScenarioInitCardiac, ScenarioInitRespiration, ScenarioInitGeneral } from '../types';
import {
  RhythmEnum,
  VpcEnum,
  VfibAmplitudeEnum,
  PulseStrengthEnum,
  HeartSoundEnum,
  LungSoundEnum,
  OnOffEnum,
  IlluminatedEnum,
  ConnectedEnum,
} from '../types';

// Defaults mirror the Django model field defaults (backend/app/models/{Cardiac,Respiration,General,Init}.py)
const defaultCardiac = (): ScenarioInitCardiac => ({
  rhythm: RhythmEnum.SINUS,
  vpc: VpcEnum.NONE,
  pea: OnOffEnum._0,
  vpc_freq: 0,
  vfib_amplitude: VfibAmplitudeEnum.LOW,
  rate: 0,
  nibp_rate: 0,
  bps_sys: 0,
  bps_dia: 0,
  left_dorsal_pulse_strength: PulseStrengthEnum.NONE,
  right_dorsal_pulse_strength: PulseStrengthEnum.NONE,
  left_femoral_pulse_strength: PulseStrengthEnum.NONE,
  right_femoral_pulse_strength: PulseStrengthEnum.NONE,
  heart_sound_volume: 0,
  heart_sound: HeartSoundEnum.NORMAL,
  ecg_indicator: IlluminatedEnum._0,
  bp_cuff: IlluminatedEnum._0,
  arrest: IlluminatedEnum._0,
});

const defaultRespiration = (): ScenarioInitRespiration => ({
  left_lung_sound: LungSoundEnum.NORMAL,
  left_lung_sound_volume: 0,
  right_lung_sound: LungSoundEnum.NORMAL,
  right_lung_sound_volume: 0,
  inhalation_duration: 500,
  exhalation_duration: 500,
  spo2: 0,
  spo2_indicator: ConnectedEnum._0,
  etco2: 0,
  etco2_indicator: ConnectedEnum._0,
  rate: 0,
  chest_movement: OnOffEnum._0,
});

const defaultGeneral = (): ScenarioInitGeneral => ({
  temperature: 975,
  temperature_enable: OnOffEnum._0,
});

export const useCreateNewScenarioInitStore = defineStore('CreateNewScenarioInitStore', {
  state: () => ({
    scenarioInit: {
      cardiac: defaultCardiac(),
      respiration: defaultRespiration(),
      general: defaultGeneral(),
      initial_scene: 1,
      record: OnOffEnum._0,
    } as ScenarioInit,
  }),
  getters: {},
  actions: {},
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useCreateNewScenarioInitStore, import.meta.hot));
}

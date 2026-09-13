import { defineStore, acceptHMRUpdate } from 'pinia';
import type { Scene, SceneInit, SceneInitCardiac, SceneInitRespiration, SceneInitGeneral } from '../types';
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

// Defaults mirror the Django model field defaults (backend/app/models/{Cardiac,Respiration,General}.py)
const defaultCardiac = (): SceneInitCardiac => ({
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

const defaultRespiration = (): SceneInitRespiration => ({
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

const defaultGeneral = (): SceneInitGeneral => ({
  temperature: 975,
  temperature_enable: OnOffEnum._0,
});

export const defaultSceneInit = (): SceneInit => ({
  cardiac: defaultCardiac(),
  respiration: defaultRespiration(),
  general: defaultGeneral(),
});

let nextSceneId = 1;

const defaultScene = (): Scene => ({
  title: 'Scene',
  id: nextSceneId++,
  triggers_needed: 1,
  init: defaultSceneInit(),
  triggers: [],
});

export const useCreateNewScenesStore = defineStore('CreateNewScenesStore', {
  state: () => ({
    scenes: [defaultScene()] as Scene[],
  }),
  getters: {
    sceneIds(state): number[] {
      return state.scenes.map((scene) => scene.id).filter((id): id is number => id !== undefined);
    },
  },
  actions: {
    addScene() {
      this.scenes.push(defaultScene());
    },
    removeScene(index: number) {
      this.scenes.splice(index, 1);
    },
    setHasTimeout(index: number, hasTimeout: boolean) {
      const scene = this.scenes[index];
      if (!scene) return;
      scene.timeout = hasTimeout ? { timeout_value: 30, scene_id: this.scenes[0]?.id ?? 1 } : undefined;
    },
    addTrigger(index: number) {
      this.scenes[index]?.triggers?.push({ scene_id: this.scenes[0]?.id ?? 1 });
    },
    removeTrigger(sceneIndex: number, triggerIndex: number) {
      this.scenes[sceneIndex]?.triggers?.splice(triggerIndex, 1);
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useCreateNewScenesStore, import.meta.hot));
}

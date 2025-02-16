/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ConnectedEnum } from './ConnectedEnum';
import type { LungSoundEnum } from './LungSoundEnum';
import type { OnOffEnum } from './OnOffEnum';
export type SceneInitRespiration = {
  left_lung_sound?: LungSoundEnum;
  left_lung_sound_volume?: number;
  right_lung_sound?: LungSoundEnum;
  right_lung_sound_volume?: number;
  inhalation_duration?: number;
  exhalation_duration?: number;
  spo2?: number;
  spo2_indicator?: ConnectedEnum;
  etco2?: number;
  etco2_indicator?: ConnectedEnum;
  rate?: number;
  chest_movement?: OnOffEnum;
};


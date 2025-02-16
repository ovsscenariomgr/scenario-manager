/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ChestMovementEnum } from './ChestMovementEnum';
import type { Etco2IndicatorEnum } from './Etco2IndicatorEnum';
import type { LeftLungSoundEnum } from './LeftLungSoundEnum';
import type { RightLungSoundEnum } from './RightLungSoundEnum';
import type { Spo2IndicatorEnum } from './Spo2IndicatorEnum';
export type ParameterTriggerRespiration = {
  left_lung_sound?: LeftLungSoundEnum;
  left_lung_sound_volume?: number;
  right_lung_sound?: RightLungSoundEnum;
  right_lung_sound_volume?: number;
  inhalation_duration?: number;
  exhalation_duration?: number;
  spo2?: number;
  spo2_indicator?: Spo2IndicatorEnum;
  etco2?: number;
  etco2_indicator?: Etco2IndicatorEnum;
  rate?: number;
  chest_movement?: ChestMovementEnum;
};


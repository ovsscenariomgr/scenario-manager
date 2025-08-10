/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
 
import type { HeartSoundEnum } from './HeartSoundEnum';
import type { IlluminatedEnum } from './IlluminatedEnum';
import type { OnOffEnum } from './OnOffEnum';
import type { PulseStrengthEnum } from './PulseStrengthEnum';
import type { RhythmEnum } from './RhythmEnum';
import type { VfibAmplitudeEnum } from './VfibAmplitudeEnum';
import type { VpcEnum } from './VpcEnum';
export type ScenarioInitCardiac = {
  rhythm?: RhythmEnum;
  vpc?: VpcEnum;
  pea?: OnOffEnum;
  vpc_freq?: number;
  vfib_amplitude?: VfibAmplitudeEnum;
  rate?: number;
  nibp_rate?: number;
  bps_sys?: number;
  bps_dia?: number;
  left_dorsal_pulse_strength?: PulseStrengthEnum;
  right_dorsal_pulse_strength?: PulseStrengthEnum;
  left_femoral_pulse_strength?: PulseStrengthEnum;
  right_femoral_pulse_strength?: PulseStrengthEnum;
  heart_sound_volume?: number;
  heart_sound?: HeartSoundEnum;
  ecg_indicator?: IlluminatedEnum;
  bp_cuff?: IlluminatedEnum;
  arrest?: IlluminatedEnum;
};


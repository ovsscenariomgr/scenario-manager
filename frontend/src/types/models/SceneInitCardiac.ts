/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ArrestEnum } from './ArrestEnum';
import type { HeartSoundEnum } from './HeartSoundEnum';
import type { LeftDorsalPulseStrengthEnum } from './LeftDorsalPulseStrengthEnum';
import type { LeftFemoralPulseStrengthEnum } from './LeftFemoralPulseStrengthEnum';
import type { PeaEnum } from './PeaEnum';
import type { RhythmEnum } from './RhythmEnum';
import type { RightDorsalPulseStrengthEnum } from './RightDorsalPulseStrengthEnum';
import type { RightFemoralPulseStrengthEnum } from './RightFemoralPulseStrengthEnum';
import type { VfibAmplitudeEnum } from './VfibAmplitudeEnum';
import type { VpcEnum } from './VpcEnum';
export type SceneInitCardiac = {
  rhythm?: RhythmEnum;
  vpc?: VpcEnum;
  pea?: PeaEnum;
  vpc_freq?: number;
  vfib_amplitude?: VfibAmplitudeEnum;
  rate?: number;
  nibp_rate?: number;
  bps_sys?: number;
  bps_dia?: number;
  left_dorsal_pulse_strength?: LeftDorsalPulseStrengthEnum;
  right_dorsal_pulse_strength?: RightDorsalPulseStrengthEnum;
  left_femoral_pulse_strength?: LeftFemoralPulseStrengthEnum;
  right_femoral_pulse_strength?: RightFemoralPulseStrengthEnum;
  heart_sound_volume?: number;
  heart_sound?: HeartSoundEnum;
  ecg_indicator?: ArrestEnum;
  bp_cuff?: ArrestEnum;
  arrest?: ArrestEnum;
};


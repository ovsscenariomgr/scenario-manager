/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */

import type { ParameterTriggerCardiac } from './ParameterTriggerCardiac';
import type { ParameterTriggerGeneral } from './ParameterTriggerGeneral';
import type { ParameterTriggerRespiration } from './ParameterTriggerRespiration';
import type { TestEnum } from './TestEnum';
/**
 * Adds nested create feature
 */
export type Trigger = {
  group?: number | null;
  scene_id?: number;
  event_id?: string | null;
  test?: TestEnum | null;
  cpr_duration?: number | null;
  cardiac?: ParameterTriggerCardiac;
  respiration?: ParameterTriggerRespiration;
  general?: ParameterTriggerGeneral;
};

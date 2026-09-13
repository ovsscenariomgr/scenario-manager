/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */

import type { OnOffEnum } from './OnOffEnum';
import type { ScenarioInitCardiac } from './ScenarioInitCardiac';
import type { ScenarioInitGeneral } from './ScenarioInitGeneral';
import type { ScenarioInitRespiration } from './ScenarioInitRespiration';
/**
 * Adds nested create feature
 */
export type ScenarioInit = {
  cardiac: ScenarioInitCardiac;
  respiration: ScenarioInitRespiration;
  general: ScenarioInitGeneral;
  initial_scene?: number;
  record?: OnOffEnum;
};

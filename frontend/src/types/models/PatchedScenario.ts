/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */

import type { EventGroup } from './EventGroup';
import type { Header } from './Header';
import type { Media } from './Media';
import type { Profile } from './Profile';
import type { ScenarioInit } from './ScenarioInit';
import type { Scene } from './Scene';
import type { Vocal } from './Vocal';
/**
 * Adds nested create feature
 */
export type PatchedScenario = {
  readonly id?: number;
  header?: Header;
  profile?: Profile;
  vocalfiles?: Array<Vocal>;
  mediafiles?: Array<Media>;
  init?: ScenarioInit;
  eventgroups?: Array<EventGroup>;
  scenes?: Array<Scene>;
};

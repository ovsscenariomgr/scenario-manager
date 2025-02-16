/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { SceneInit } from './SceneInit';
import type { Timeout } from './Timeout';
import type { Trigger } from './Trigger';
/**
 * Adds nested create feature
 */
export type Scene = {
  title?: string;
  id?: number;
  triggers_needed?: number;
  timeout: Timeout;
  init: SceneInit;
  triggers: Array<Trigger>;
};

